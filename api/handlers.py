from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseGone

from tastypie import fields
from tastypie.authorization import Authorization, ReadOnlyAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.utils import trailing_slash

from books.models import Booklist, Book

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['username', 'password', 'is_superuser']
    
class BooklistResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')
    books = fields.ToManyField('api.handlers.BookResource', 'book_set')
    filtering = {
            'id': ALL_WITH_RELATIONS
        }
    
    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/books%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_books'), name="api_get_books"),
        ]
        
    def get_books(self, request, **kwargs):
        try:
            obj = self.cached_obj_get(request=request, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpResponseGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")
    
        details = BookResource().get_list(request, booklist = obj)
        
        return details

    class Meta:
        queryset = Booklist.objects.all()
        resource_name = 'booklist'
        authorization = Authorization() if settings.DEBUG else ReadOnlyAuthorization()
        always_return_data = True
    
class BookResource(ModelResource):
    booklist = fields.ToOneField(BooklistResource, 'booklist')
    
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        authorization = Authorization() if settings.DEBUG else ReadOnlyAuthorization()
        always_return_data = True
        filtering = {
            'booklist': ALL_WITH_RELATIONS
        }
        