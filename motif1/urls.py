from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('contact',views.contact,name="contact"),
    path('blog',views.blog,name="blog"),
    path('blog-details',views.blog_details,name="blog-details"),
    path('delete-comment/<int:comment_id>/',views.delete_comment,name="delete-comment"),
    
    
    
]