from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse_lazy

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,"blog/home.html",context)
    # return HttpResponse("<h1>Blog home</h1")

#Class based view
class PostListView(ListView):
    model=Post
    #To tell Django to look for template here,since we are referring to the already created home.html
    template_name ="blog/home.html"  #<app>/<model>_<viewtype>.html
    #Override the default "object_list" name it would be given, to "posts" as above
    context_object_name ="posts"
    #Setting the posts order from newest to oldest
    ordering =["-date_posted"]
    #Setting number of posts per page
    paginate_by = 5

#View for seeing all the posts by a specific user
class UserPostListView(ListView):
    model=Post
    template_name ="blog/user_posts.html"  #<app>/<model>_<viewtype>.html
    context_object_name ="posts"
    paginate_by = 5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")

#In this one, we are trying to stick with the default naming and directories of the class view
class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView): #Ensures login is required to create post
    #This view would need form fields since new blog is being created
    model=Post
    fields=["title","content"]

    #Function to override the validation process, inserting the user as author before validating
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form) #returns the form and now validates it

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): #Ensures login is required to update post
    model=Post
    fields=["title","content"]
    
    #Function to override the validation process, inserting the user as author before validating
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form) #returns the form and now validates it

    #Function that ensures only post authors can update a post
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url=reverse_lazy("blog-home") #Can you put in the URL name here? *Done with reverse lazy*

    #Function that ensures only post authors can update a post
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,"blog/about.html",{"title":"About"})
    # return HttpResponse("<h1>Blog about</h1")