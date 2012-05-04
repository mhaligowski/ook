from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseGone

from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.utils import trailing_slash

from auth import DjangoAuthorization, ApiKeyAuthentication

from books.models import Booklist, Book

class UserResource(ModelResource):
    class Meta:
        list_allowed_methods = ['get',]
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['username', 'password', 'is_superuser']
        
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

class BookResource(ModelResource):
    booklist = fields.ToOneField('api.handlers.BooklistResource', 'booklist')
    
    class Meta:
        list_allowed_methods = ['get', 'post', 'put', 'delete',]
        queryset = Book.objects.all()
        resource_name = 'book'
        always_return_data = True
        filtering = {
            'booklist': ALL_WITH_RELATIONS
        }
        
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        
    def override_urls(self):
        return [
            url(r"^booklist/(?P<booklist_pk>[\d]*)/(?P<resource_name>%s)/$" % self._meta.resource_name, self.wrap_view('dispatch_list'), name="api_dispatch_list"),
        ]
    
class BooklistResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')
    books = fields.ToManyField('api.handlers.BookResource', 'book_set', null=True, blank=True)
    filtering = {
            'id': ALL_WITH_RELATIONS
        }
    
    class Meta:
        list_allowed_methods = ['get', 'post', 'put', 'delete',]
        queryset = Booklist.objects.all()
        resource_name = 'booklist'
        always_return_data = True

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
            
