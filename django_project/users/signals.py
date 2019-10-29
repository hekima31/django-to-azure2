from django.db.models.signals import post_save #signal that gets fired after an object is saved
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#Allows a simultaneous creation of profile when a new user is created.
#When a user is created, a signal is sent to the receiver.
#If the user is created, it creates a profile from the user instance.
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

#Saves the user profile created above
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
