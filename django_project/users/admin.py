from django.contrib import admin
from .models import Profile

# Register your models here to be managed in the admin page.


#Register the profile model on the admin(That it can be managed)
admin.site.register(Profile)

