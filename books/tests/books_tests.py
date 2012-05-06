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
        
    def test_create_book_for_non_owner_booklist(self):
        bl = Booklist.objects.create(
            name = "test booklist",
            owner = self.user1,
        )
        
        self.assertTrue(self.user1.has_perm('books.add_book_to_booklist', bl))
        self.assertFalse(self.user2.has_perm('books.add_book_to_booklist', bl))
        
        
class ApiTest(TestCase):
    def create_book(self, user, title, author, isbn, booklist):
        api_string = "ApiKey %s:%s" % (user.username, user.api_key.key)
        url = "/api/v1/booklist/%d/book/" % booklist.pk

        data = json.dumps({
            'title': title,
            'author': author,
            'isbn': isbn,
            'booklist': "/api/v1/booklist/%d/" % booklist.pk
        })
        
        return self.client.post(url,
                                data,
                                content_type = "application/json",
                                ACCEPT = "application/json",
                                HTTP_AUTHORIZATION = api_string,
                                HTTP_X_REQUESTED_WITH = "XMLHttpRequest")

    def update_book(self, book_pk, user, title, author, isbn, booklist):
        api_string = "ApiKey %s:%s" % (user.username, user.api_key.key)
        
        url = reverse('api_dispatch_detail',
                      kwargs={'api_name':'v1',
                              'resource_name': 'book',
                              'pk': book_pk})

        data = json.dumps({
            'title': title,
            'author': author,
            'isbn': isbn,
            'booklist': reverse('api_dispatch_detail',
                             kwargs={'pk': booklist.pk,
                                     'api_name': 'v1',
                                     'resource_name': 'booklist'})
        })

        return self.client.put(url,
                               data,
                               content_type = "application/json",
                               HTTP_AUTHORIZATION = api_string,
                               HTTP_X_REQUESTED_WITH = "XMLHttpRequest")


    def setUp(self):
        self.client = Client()
        
        self.user1 = User.objects.create_user('user1', 'user@user.com', 'passw0rd')
        self.booklist1 = Booklist.objects.create(
            name = "booklist1",
            owner = self.user1
        )
        
        self.booklist3 = Booklist.objects.create(
            name = "booklist3",
            owner = self.user1
        )
        
        self.user2 = User.objects.create_user('user2', 'user@user.com', 'passw0rd')
        self.booklist2 = Booklist.objects.create(
            name = "booklist2",
            owner = self.user2
        )

    def test_create_book_to_owner_list(self):
        """
        User should be able to create new book for his booklist with a POST
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

    def test_create_book_to_other_list(self):
        """
        User should be unable to create new book for other users's booklist with a POST
        """
        response = self.create_book(user = self.user2,
                            title = "test",
                            author = "John Doe",
                            isbn = 123,
                            booklist = self.booklist1)

        self.assertEqual(response.status_code, 401)

    def delete_book(self, user, pk):
        api_string = "ApiKey %s:%s" % (user.username, user.api_key.key)
        
        url = reverse('api_dispatch_detail',
                      kwargs={'api_name':'v1',
                              'resource_name': 'book',
                              'pk': pk})

        return self.client.delete(url,
                                  HTTP_AUTHORIZATION = api_string,
                                  HTTP_X_REQUESTED_WITH = "XMLHttpRequest")
        
    def test_edit_own_book(self):
        """
        User should be able to edit book he created
        """
        # create book
        b = Book.objects.create(
            title = "test",
            author = "John Doe",
            isbn = 123,
            booklist = self.booklist1
        )
        
        response = self.update_book(
            book_pk = b.pk,
            user = self.user1,
            title = "updated test",
            author = "John Doe",
            isbn = 123,
            booklist = self.booklist1
        )
        
        # confirm status
        self.assertEqual(response.status_code, 202)
        
        # redownload the book
        b = Book.objects.get(pk = b.pk)
        self.assertEqual(b.title, "updated test")
        
    def test_edit_other_book(self):
        """
        User should be unable to edit book other user created
        """
        # create book
        b = Book.objects.create(
            title = "test",
            author = "John Doe",
            isbn = 123,
            booklist = self.booklist1
        )
        
        response = self.update_book(
            book_pk = b.pk,
            user = self.user2,
            title = "updated test",
            author = "John Doe",
            isbn = 123,
            booklist = self.booklist1
        )
        
        # confirm status
        self.assertEqual(response.status_code, 401)

    def test_edit_booklist_to_other_user(self):
        """
        User should be unable to move book he created to booklist of other user
        """
        # create book
        b = Book.objects.create(
            title = "test",
            author = "John Doe",
            isbn = 123,
            booklist = self.booklist1
        )
        
        response = self.update_book(
            book_pk = b.pk,
            user = self.user1,
            title = "updated test",
            author = "John Doe",
            isbn = 123,
            booklist = self.booklist2
        )

        self.assertEqual(response.status_code, 401)
        
    def test_delete_book_of_user(self):
        # create book
        b = Book.objects.create(
            title = "test",
            author = "John Doe",
            isbn = 123,
            booklist = self.booklist1
        )

        response = self.delete_book(
            user = self.user1,
            pk = b.pk
        )
        
        self.assertEqual(response.status_code, 204)
        
    def test_delete_book_of_other_user(self):
        # create book
        b = Book.objects.create(
            title = "test",
            author = "John Doe",
            isbn = 123,
            booklist = self.booklist1
        )

        response = self.delete_book(
            user = self.user2,
            pk = b.pk
        )
        
        self.assertEqual(response.status_code, 401)

    def test_create_book_to_different_booklists(self):
        """
        Try creating a booklist with address /api/v1/booklist/[booklist1.pk]/books,
        but with parent for booklist3. Should fail with HTTP response 400 Bad request.
        """
        api_string = "ApiKey %s:%s" % (self.user1.username, self.user1.api_key.key)
        url = "/api/v1/booklist/%d/book/" % self.booklist1.pk

        data = json.dumps({
            'title': "aBook",
            'author': "anAuthor",
            'isbn': "123",
            'booklist': "/api/v1/booklist/%d/" % self.booklist3.pk
        })
        
        response = self.client.post(url,
                                    data,
                                    content_type = "application/json",
                                    ACCEPT = "application/json",
                                    HTTP_AUTHORIZATION = api_string,
                                    HTTP_X_REQUESTED_WITH = "XMLHttpRequest")
        
        self.assertEqual(response.status_code, 400)

    def test_create_book_to_same_booklists(self):
        """
        Try creating a booklist with address /api/v1/booklist/[booklist3.pk]/books,
        but with parent for booklist3. Should fail with HTTP response 400 Bad request.
        """
        api_string = "ApiKey %s:%s" % (self.user1.username, self.user1.api_key.key)
        url = "/api/v1/booklist/%d/book/" % self.booklist1.pk

        data = json.dumps({
            'title': "aBook",
            'author': "anAuthor",
            'isbn': "123",
            'booklist': "/api/v1/booklist/%d/" % self.booklist1.pk
        })
        
        response = self.client.post(url,
                                    data,
                                    content_type = "application/json",
                                    ACCEPT = "application/json",
                                    HTTP_AUTHORIZATION = api_string,
                                    HTTP_X_REQUESTED_WITH = "XMLHttpRequest")
        
        self.assertEqual(response.status_code, 201)
