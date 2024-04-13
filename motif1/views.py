from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import Team,Contact,BlogPost, Comment, Faq
from datetime import datetime 
from django.utils import timezone



# Create your views here.


def index(request): 
    
    team_profiles = Team.objects.all()
    faqs = Faq.objects.all()
    context = {'team_profiles' : team_profiles , 'faqs' : faqs }


        
    return render(request,"index.html",context)

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"This Email already exists")
                return redirect('signup')
            elif User.objects.filter(username=email).exists():
                messages.info("This Username already exist")
                return redirect('signup')
            else:
               user = User.objects.create_user(username=name,password=password,email=email)
               user.save()
               return redirect('login')
        else:
            messages.info(request,"Passwords do not match")
            return redirect('signup')

    return render(request,"signup.html")

def login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name , password=password)
        
        if user is not None:

            auth.login(request,user)
            return redirect ('/')
        
        else:
            messages.info(request,"Invalid Credentials")
            return redirect ('login')
        
    else:
         return render(request,"indice.html")


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        user = name 

        contact_obj = Contact.objects.create(user=user,name=name,email=email,subject=subject,message=message)
        contact_obj.save()
        messages.info(request,"Thank you for contacting us! We will reply you shortly.")

        return redirect('/')

    else:
        return redirect('/')
    return render(request,"index.html")

@login_required(login_url="login")
def blog(request):

    blog_posts = BlogPost.objects.all()
    context = {'blog_posts' : blog_posts}

    return render(request,"blog.html",context)

@login_required(login_url="login")
def blog_details(request):
    commenter = request.user.username
    commenter_email  = request.user.email
    if request.method == "POST" :
        comment = request.POST['comment']
        post_id = request.POST['post_id']
        if BlogPost.objects.filter(id=post_id).exists():
            comments = Comment.objects.create(comment_name=commenter,email=commenter_email,comment=comment,post_id=post_id)
            comments.save()
            return redirect('blog-details')
        else:
            messages.info(request, "This Post ID dosen't exist")
    else:
            pass
    
    
    blog_posts = BlogPost.objects.all()
    comment_objs = Comment.objects.all()
    comment_number = len(comment_objs)
    context = {'blog_posts' : blog_posts, 'comment_number' : comment_number, 'comment_objs' : comment_objs, }
    return render(request,"blog-details.html",context)

def delete_comment(request,comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.comment_name == request.user.username:
        comment.delete()
    return redirect('blog-details')