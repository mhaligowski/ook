# -*- coding: utf-8 -*-

from django.core import management
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ObjectDoesNotExist

import json
from books.models import Booklist, Book

class BooklistsTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.user1 = User.objects.create_user('user1', 'user@user.com', 'passw0rd')
        self.user2 = User.objects.create_user('user2', 'user@user.com', 'passw0rd')

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
        