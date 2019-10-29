from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

urlpatterns = [
    #Need to convert class to view with the as_view method
    path("", PostListView.as_view(),name="blog-home"),
    path("user/<str:username>", UserPostListView.as_view(),name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(),name="post-detail"), #pk is primary key, identifying each post
    path("post/new/", PostCreateView.as_view(),name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(),name="post-update"), #Create and update urls are using the same post_form template
    path("post/<int:pk>/delete/", PostDeleteView.as_view(),name="post-delete"), 
    path('about/', views.about,name="blog-about"),
]

