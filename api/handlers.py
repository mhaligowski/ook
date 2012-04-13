from django.contrib.auth.models import User
from django.conf import settings

from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization, ReadOnlyAuthorization

from books.models import Booklist, Book

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['username', 'password', 'is_superuser']

class BooklistRichResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')
    books = fields.ToManyField('api.handlers.BookResource', 'book_set', full=True)

    class Meta:
        queryset = Booklist.objects.all()
        resource_name = 'booklist_data'
        filtering = {
            'id': ALL_WITH_RELATIONS
        }
    
class BooklistResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')

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
        filtering = {
            'booklist': ALL_WITH_RELATIONS
        }
        