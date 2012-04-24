from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Booklist(models.Model):
    """
    Booklist model
    """
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now = True, default = '1900-01-01')
    is_default = models.BooleanField(default = False)
    navbar_order = models.PositiveSmallIntegerField(default = 0) # sorting by desc navbar_order
    
    class Meta:
        permissions = (
            ('view_booklist', 'View a booklist'),
            ('add_book_to_booklist', 'Add a book to the booklist'),
        )
    
class Book(models.Model):
    """
    Book model
    """
    title = models.CharField(max_length=2000)
    author = models.CharField(max_length=2000)
    isbn = models.CharField(max_length=2000)
    booklist = models.ForeignKey(Booklist)

###
# SIGNALS
###

def create_default_booklist(sender, instance, created, **kwargs):
    """
    Create default booklist when the user is created
    """
    if created and instance.pk != -1:
        Booklist.objects.create(name = "[]",
                                owner = instance,
                                is_default = True)
post_save.connect(create_default_booklist, sender=User)

def assign_booklist_permission(sender, instance, created, **kwargs):
    """
    Assign permissions to the owner of the booklist when the booklist is created
    """
    if created:
        from guardian.shortcuts import assign
        
        perms = [
            'books.change_booklist',
            'books.delete_booklist',
            'books.add_book_to_booklist',
        ]
        for perm in perms:
            assign(perm, instance.owner, instance)

post_save.connect(assign_booklist_permission, sender=Booklist)

def assign_book_permission(sender, instance, created, **kwargs):
    """
    Assign permissions to the booklist owner when the book is created
    """
    if created:
        from guardian.shortcuts import assign
        assign('books.change_book', instance.booklist.owner, instance)
        assign('books.delete_book', instance.booklist.owner, instance)
        
post_save.connect(assign_book_permission, sender=Book)
