from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booklist(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now = True, default = '1900-01-01')
    is_default = models.BooleanField(default = False)
    navbar_order = models.PositiveSmallIntegerField(default = 0) # sorting by desc navbar_order