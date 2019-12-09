from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # No brackets in the timezone function because it is the function that is
    date_posted = models.DateTimeField(default=timezone.now)
    # required
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    # Telling the function how the Post function should be returned
    # To return it in readable format
    def __str__(self):
        return self.title

   # Allows for redirect to the detail view of the blog instance just created
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
