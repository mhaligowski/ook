# -*- coding: utf-8 -*-

from django.core import management
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ObjectDoesNotExist

import json
from books.models import Booklist, Book

class BooksTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.user1 = User.objects.create_user('user1', 'user@user.com', 'passw0rd')
        self.user2 = User.objects.create_user('user2', 'user@user.com', 'passw0rd')

    def test_can_create_book(self):
        self.assertTrue(self.user1.has_perm('books.add_book'))
        self.assertTrue(self.user2.has_perm('books.add_book'))

    def test_can_edit_own_book(self):
        bl = Booklist.objects.create(
            name = "test booklist",
            owner = self.user1,
        )
        
        book = Book.objects.create(
            title = u'Mistrz i Małgorzata',
            author = u'Mihaił Bułhakow',
            isbn = 123456,
            booklist = bl
        )

        self.assertTrue(self.user1.has_perm('books.change_book', book))
        self.assertFalse(self.user2.has_perm('books.change_book', book))

        self.assertTrue(self.user1.has_perm('books.delete_book', book))
        self.assertFalse(self.user2.has_perm('books.delete_book', book))
        
class ApiTest(TestCase):
    def create_book(self, user, title, author, isbn, booklist):
        api_string = "ApiKey %s:%s" % (user.username, user.api_key.key)
        url = reverse('api_dispatch_list',
                      kwargs={'api_name':'v1',
                              'resource_name': 'book'})

        data = json.dumps({
            'title': title,
            'author': author,
            'isbn': isbn,
            'booklist': reverse('api_dispatch_detail',
                             kwargs={'pk': booklist.pk,
                                     'api_name': 'v1',
                                     'resource_name': 'booklist'})
        })
        
        return self.client.post(url,
                                data,
                                content_type = "application/json",
                                ACCEPT = "application/json",
                                HTTP_AUTHORIZATION = api_string,
                                HTTP_X_REQUESTED_WITH = "XMLHttpRequest")

    def setUp(self):
        self.client = Client()
        
        self.user1 = User.objects.create_user('user1', 'user@user.com', 'passw0rd')
        self.booklist1 = Booklist.objects.create(
            name = "booklist1",
            owner = self.user1
        )
        self.user2 = User.objects.create_user('user2', 'user@user.com', 'passw0rd')

    def test_create_book_to_owner_list(self):
        """
        User should be able to create new booklist with a POST
        """
        response = self.create_book(user = self.user1,
                                    title = "test",
                                    author = "John Doe",
                                    isbn = 123,
                                    booklist = self.booklist1)
        self.assertEqual(response.status_code, 201)
        
        # parse the response
        return_data = json.loads(response.content)
        self.assertEquals(return_data['title'], 'test')
        
        # now check the django-side
        b = Book.objects.get(pk = return_data["id"])
        self.assertEquals(b.title, 'test')
        self.assertEquals(b.booklist.owner, self.user1)
