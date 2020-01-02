from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Models are similar to tables in database. They have a relational property

# Appending a profile segment to the built-in user variable


class Profile(models.Model):
    # This is so as to extend the user variable in Django by linking it to a profile
    # Cascade (effect) means when a user is deleted, their proifle is also deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # You can also choose to add other fields such as a bio field etc.
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

# dunder str method tells the class how it should display itself when returned
    def __str__(self):
        return f"{self.user.username} Profile"

    # def save(self, *args, **kwargs):#Parent save function run normally when profile is created/updated
    #     super().save(*args, **kwargs)

    #     img=Image.open(self.image.path) #grabs image from path

    #     if img.height > 300 or img.width > 300:
    #         output_size=(300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path) #creates new image instance on the same path (not deleting the previous image)

    # Commented out as it causes problems when used with AWS S3 and Azure File Storage
