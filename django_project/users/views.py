from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

#Renders the registration page online to allow new users to register
def register(request):
    if request.method == "POST": #Checks if there is new data passed in from the forms
        form=UserRegisterForm(request.POST)
        if form.is_valid(): #Checks if the data entered has no input errors
            form.save()
            username= form.cleaned_data.get('username') # Grabs the username from the submitted form if valid
            messages.success(request,f"Your account has been created! You are now able to log in")
            return redirect("login") #Redirects to specified URL
    else:
        form=UserRegisterForm()

    return render(request,"users/register.html",{"form":form})


#Function below renders the profile page online.
#Decorator allows access to this view only if logged in else redirects to URL
@login_required
def profile(request):
    if request.method == "POST":
        #Creating an instance of the UserUpdate and Profile forms populated with the current user details
        u_form=UserUpdateForm(request.POST,instance=request.user) 
        p_form=ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile) #file accounts for the image uploaded
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your account has been succesfully updated!")
            return redirect("profile") #Redirecting here avoids post-get redirect pattern
    else:
        u_form=UserUpdateForm(instance=request.user) 
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        "u_form":u_form, #Can't assign to string literal (Makes sense to use semicolon and not "=")
        "p_form":p_form
    }

    return render(request,"users/profile.html",context)