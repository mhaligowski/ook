from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile

# Create your models here.
class UserProfile(UserenaBaseProfile):
    # user reference
    user = models.OneToOneField(User)
    
    facebook_id = models.CharField(max_length = 128, blank = True, null = True)