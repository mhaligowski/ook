from django.db import models
from django.contrib.auth.models import User, Group
from userena.models import UserenaBaseProfile
from django.db.models.signals import post_save
from tastypie.models import create_api_key

class UserProfile(UserenaBaseProfile):
    # user reference
    user = models.OneToOneField(User)
    
    facebook_id = models.CharField(max_length = 128, blank = True, null = True)
    
    class Meta:
        permissions = (
            ('change_profile', 'Change profile'),
            ('view_profile', 'View profile'),
            ('delete_profile', 'Delete profile'),
        )
        
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create user profie and set the permissions
    """
    if created and instance.pk >= 0:
        UserProfile.objects.create(user=instance)
        
        # get default group, but not for anonymous
        try:
            default_group = Group.objects.get(name = "default_users")
            instance.groups.add(default_group)
        except:
            pass
        
post_save.connect(create_user_profile, sender=User)

# generate api key for the user when the user is created
post_save.connect(create_api_key, sender=User)