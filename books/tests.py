# -*- encoding: utf-8 -*-

from django.core import management
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group, Permission
import json
import models

class BooklistsTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.user1 = User.objects.create_user('user1', 'user@user.com', 'passw0rd')
        self.user2 = User.objects.create_user('user2', 'user@user.com', 'passw0rd')

    def test_initial_permissions(self):
        """
        User should have the permission to create a new booklist
        """
        
        # user can create new booklists...
        self.assertTrue(self.user1.has_perms([
            'books.add_booklist',
            'books.view_booklist',
            ]
            )
        )
        
        # ... but can't edit them
        self.assertFalse(self.user1.has_perm('books.change_booklist'))

    def test_new_user_has_a_default_booklist(self):
        """
        When creating a user, a default booklist with name '[]' should be created
        """
        
        # create brand new user
        newUser = User.objects.create_user('newUser', 'newUser@example.com', 'passw0rd')
        
        # assert that he has exactly one booklist...
        self.assertEqual(newUser.booklist_set.count(), 1)
        
        # ...and that it's the default one
        b = newUser.booklist_set.only()[0]
        self.assertTrue(b.is_default)
        self.assertEquals(u'[]', b.name)
        
    def test_can_edit_own_booklist(self):
        """
        User should have permission to edit his or her own booklist
        """
        b = models.Booklist.objects.create(
            name = "test booklist",
            owner = self.user1,
        )
        
        self.assertTrue(self.user1.has_perm('books.change_booklist', b))
        self.assertFalse(self.user2.has_perm('books.change_booklist', b))
        
        self.assertTrue(self.user1.has_perm('books.delete_booklist', b))
        self.assertFalse(self.user2.has_perm('books.delete_booklist', b))
        
    def test_can_edit_own_book(self):
        bl = models.Booklist.objects.create(
            name = "test booklist",
            owner = self.user1,
        )
        
        book = models.Book.objects.create(
            title = u'Mistrz i Małgorzata',
            author = u'Mihaił Bułhakow',
            isbn = 123456,
            booklist = bl
        )

        self.assertTrue(self.user1.has_perm('books.change_book', book))
        self.assertFalse(self.user2.has_perm('books.change_book', book))

        self.assertTrue(self.user1.has_perm('books.delete_book', book))
        self.assertFalse(self.user2.has_perm('books.delete_book', book))
        
class BooklistApiTestCase(TestCase):
    def create_booklist(self, name, user):
        api_string = "ApiKey %s:%s" % (user.username, user.api_key.key)
        url = reverse('api_dispatch_list',
                      kwargs={'api_name':'v1',
                              'resource_name': 'booklist'})

        data = json.dumps({
            'name': "test",
            'owner': reverse('api_dispatch_detail',
                             kwargs={'pk': user.pk,
                                     'api_name': 'v1',
                                     'resource_name': 'auth/user'})
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
        self.user2 = User.objects.create_user('user2', 'user@user.com', 'passw0rd')

    def test_create_new_booklist(self):
        """
        User should be able to create new booklist with a POST
        """
        response = self.create_booklist("test", self.user1)
        
        self.assertEqual(response.status_code, 201)
        
        # parse the response
        return_data = json.loads(response.content)
        self.assertEquals(return_data['name'], 'test')
        
        # now check the django-side
        b = models.Booklist.objects.get(pk = return_data["id"])
        self.assertEquals(b.name, 'test')
        self.assertEquals(b.owner, self.user1)

