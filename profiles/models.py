from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile
from django.db.models.signals import post_save

class UserProfile(UserenaBaseProfile):
    # user reference
    user = models.OneToOneField(User)
    
    facebook_id = models.CharField(max_length = 128, blank = True, null = True)
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
post_save.connect(create_user_profile, sender=User)