from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseGone

from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.utils import trailing_slash

from auth import DjangoAuthorization, ApiKeyAuthentication

from books.models import Booklist, Book

import validation

class UserResource(ModelResource):
    class Meta:
        list_allowed_methods = ['get',]
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['username', 'password', 'is_superuser']
        
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

    
class BooklistResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')
    books = fields.ToManyField('api.handlers.BookResource', 'book_set', null=True, blank=True)
    
    class Meta:
        list_allowed_methods = ['get', 'post', 'put', 'delete',]
        queryset = Booklist.objects.all()
        resource_name = 'booklist'
        always_return_data = True

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

        filtering = {
                'id': ALL_WITH_RELATIONS
            }
            
class BookResource(ModelResource):
    booklist = fields.ToOneField(BooklistResource, 'booklist')
    
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
        validation = validation.BookValidation()
        
    def override_urls(self):
        return [
            url(r"^(?P<parent_resource_name>%s)/(?P<parent_pk>[\d]*)/(?P<resource_name>%s)/$" % (self.booklist.to._meta.resource_name, self._meta.resource_name),
                self.wrap_view('parental_dispatch_list'),
                name="api_dispatch_list"),
            url(r"^(?P<parent_resource_name>%s)/(?P<parent_pk>[\d]*)/(?P<resource_name>%s)/(?P<pk>[\d]*)/$" % (self.booklist.to._meta.resource_name, self._meta.resource_name),
                self.wrap_view('parental_dispatch_detail'),
                name="api_dispatch_detail"),
        ]

    def convert_parental_to_param(self, url_dict):
        url_copy = url_dict.copy()
        
        # the parental stuff is already here
        
        # first, add the new key
        key_name = "%s__id" % url_copy["parent_resource_name"]
        
        url_copy[key_name] = url_copy["parent_pk"]
        
        # then, remove the unused keys
        del url_copy["parent_resource_name"]
        del url_copy["parent_pk"]

        return url_copy
        
    def parental_dispatch_detail(self, request, **kwargs):
        return self.dispatch('detail', request, **self.convert_parental_to_param(kwargs))

    def parental_dispatch_list(self, request, **kwargs):
        return self.dispatch('list', request, **self.convert_parental_to_param(kwargs))
