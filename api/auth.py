from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.http import HttpUnauthorized
from django.core.urlresolvers import resolve

class DjangoAuthorization(Authorization):
    """
    Uses permission checking from ``django.contrib.auth`` to map
    ``POST / PUT / DELETE / PATCH`` to their equivalent Django auth
    permissions.
    
    Overriden for Ook
    """
    def is_authorized(self, request, object=None):
        # GET-style methods are always allowed.
        if request.method in ('OPTIONS', 'HEAD'):
            return True

        klass = self.resource_meta.object_class

        # If it doesn't look like a model, we can't check permissions.
        if not klass or not getattr(klass, '_meta', None):
            return True

        permission_map = {
            'GET': '%s.view_%s',
            'POST': '%s.add_%s',
            'PUT': '%s.change_%s',
            'DELETE': '%s.delete_%s'
        }
        
        # If we don't recognize the HTTP method, we don't know what
        # permissions to check. Deny.
        if request.method not in permission_map:
            return False

        permission_code = permission_map[request.method] % (klass._meta.app_label, klass._meta.module_name)

        if not hasattr(request, 'user'):
            return False

        url = resolve(request.path)
        if url.url_name == "api_dispatch_detail":
            # get object
            obj = klass.objects.get(pk=url.kwargs["pk"])
            return request.user.has_perm(permission_code, obj)
        else:
            return request.user.has_perm(permission_code)

class ApiKeyAuthentication(Authentication):
    """
    Handles API key auth, in which a user provides a username & API key.

    Uses the ``ApiKey`` model that ships with tastypie. If you wish to use
    a different model, override the ``get_key`` method to perform the key check
    as suits your needs.
    """
    def _unauthorized(self):
        return HttpUnauthorized()

    def extract_credentials(self, request):
        if request.META.get('HTTP_AUTHORIZATION') and request.META['HTTP_AUTHORIZATION'].lower().startswith('apikey '):
            (auth_type, data) = request.META['HTTP_AUTHORIZATION'].split()

            if auth_type.lower() != 'apikey':
                raise ValueError("Incorrect authorization header.")

            username, api_key = data.split(':', 1)
        else:
            username = request.GET.get('username') or request.POST.get('username')
            api_key = request.GET.get('api_key') or request.POST.get('api_key')

        return username, api_key

    def is_authenticated(self, request, **kwargs):
        """
        Finds the user and checks their API key.

        Should return either ``True`` if allowed, ``False`` if not or an
        ``HttpResponse`` if you need something custom.
        """
        from django.contrib.auth.models import User

        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()

        if not username or not api_key:
            return self._unauthorized()

        try:
            user = User.objects.get(username=username)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()

        request.user = user
        return self.get_key(user, api_key)

    def get_key(self, user, api_key):
        """
        Attempts to find the API key for the user. Uses ``ApiKey`` by default
        but can be overridden.
        """
        from tastypie.models import ApiKey

        try:
            ApiKey.objects.get(user=user, key=api_key)
        except ApiKey.DoesNotExist:
            return self._unauthorized()

        return True

    def get_identifier(self, request):
        """
        Provides a unique string identifier for the requestor.

        This implementation returns the user's username.
        """
        username, api_key = self.extract_credentials(request)
        return username or 'nouser'
