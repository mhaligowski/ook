from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from books.models import Booklist, Book

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['username', 'password', 'is_superuser']

class BooklistResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')
    books = fields.ToManyField('api.handlers.BookResource', 'book_set', full=True)

    class Meta:
        queryset = Booklist.objects.all()
        resource_name = 'booklist'
        filtering = {
            'id': ALL_WITH_RELATIONS
        }

class BookResource(ModelResource):
    booklist = fields.ToOneField(BooklistResource, 'booklist')
    
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        filtering = {
            'booklist': ALL_WITH_RELATIONS
        }
        