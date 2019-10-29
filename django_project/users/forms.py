from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#Here we can append custom fields to existing in-built variables such as User and Forms

#This requires us to create a new form 
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField() #Defining the email field to append to the form

    class Meta:
        model = User
        fields=["username","email","password1","password2"]

#Allows for update of username and password
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields=["username","email"]


#Allows for updating the profile picture
class ProfileUpdateForm(forms.ModelForm): #No adding additional fields here
    class Meta:
        model = Profile
        fields=["image"]
