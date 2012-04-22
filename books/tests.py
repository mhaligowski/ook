from django.core import management
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group, Permission

import models

class BooklistsTest(TestCase):
    def setUp(self):
        self.client = Client()
        management.call_command('check_permissions')
        
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
        
        self.assertTrue(self.user1.has_perm('books.change_booklist', b))
        self.assertFalse(self.user2.has_perm('books.delete_booklist', b))
        