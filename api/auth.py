from tastypie.authorization import Authorization

class DjangoAuthorization(Authorization):
    """
    Uses permission checking from ``django.contrib.auth`` to map
    ``POST / PUT / DELETE / PATCH`` to their equivalent Django auth
    permissions.
    
    Overriden for Ook
    """
    def is_authorized(self, request, object=None):
        print "Look Ma, I'm authorizing! And the object is: %s" % object
        # GET-style methods are always allowed.
        if request.method in ('GET', 'OPTIONS', 'HEAD'):
            return True

        klass = self.resource_meta.object_class

        # If it doesn't look like a model, we can't check permissions.
        if not klass or not getattr(klass, '_meta', None):
            return True

        permission_map = {
            'POST': ['%s.add_%s'],
            'PUT': ['%s.change_%s'],
            'DELETE': ['%s.delete_%s'],
            'PATCH': ['%s.add_%s', '%s.change_%s', '%s.delete_%s'],
        }
        permission_codes = []

        # If we don't recognize the HTTP method, we don't know what
        # permissions to check. Deny.
        if request.method not in permission_map:
            return False

        for perm in permission_map[request.method]:
            permission_codes.append(perm % (klass._meta.app_label, klass._meta.module_name))

        if not hasattr(request, 'user'):
            return False

        return request.user.has_perms(permission_codes)
