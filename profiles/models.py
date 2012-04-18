from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile
from django.db.models.signals import post_save
from tastypie.models import create_api_key

class UserProfile(UserenaBaseProfile):
    # user reference
    user = models.OneToOneField(User)
    
    facebook_id = models.CharField(max_length = 128, blank = True, null = True)
    
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create user profie and set the permissions
    """
    if created:
        UserProfile.objects.create(user=instance)
        
post_save.connect(create_user_profile, sender=User)

# generate api key for the user when the user is created
post_save.connect(create_api_key, sender=User)