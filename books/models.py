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
        )
    
    
class Book(models.Model):
    """
    Book model
    """
    title = models.CharField(max_length=2000)
    author = models.CharField(max_length=2000)
    isbn = models.CharField(max_length=2000)
    booklist = models.ForeignKey(Booklist)
    

def create_default_booklist(sender, instance, created, **kwargs):
    """
    Create default booklist when the user is created
    """
    if created:
        Booklist.objects.create(name = "[]",
                                owner = instance,
                                is_default = True)
        
        
post_save.connect(create_default_booklist, sender=User)