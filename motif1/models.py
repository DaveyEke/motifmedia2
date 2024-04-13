from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
User = get_user_model()

# Create your models here.

class Team(models.Model):
    user = models.CharField(max_length=200)
    team_name = models.TextField(blank=True)
    id_user = models.AutoField(primary_key=True)
    skill = models.TextField(blank=True)
    image = models.ImageField(upload_to='team_images')
    linkedin =models.TextField(blank=True)
    Twitter = models.TextField(blank=True)
    Instagram = models.TextField(blank=True)

    def __str__(self):
        return self.team_name


class Contact(models.Model):
    user = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.subject


class BlogPost(models.Model):
    author_name = models.CharField(max_length=150)
    user = models.CharField(max_length=150)
    title = models.TextField()
    category = models.CharField(max_length=150)
    author_img = models.ImageField(upload_to="author_images")
    date = models.DateTimeField(default=datetime.now)
    post_image = models.ImageField(upload_to="post_images")
    post_content = models.TextField()
    author_twitter = models.TextField(blank=True)
    author_linkedin = models.TextField(blank=True)
    author_instagram = models.TextField(blank=True)
    author_bio = models.TextField(blank=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user

class Comment(models.Model):
    comment_name = models.CharField(max_length = 100)
    date = models.DateTimeField(default=datetime.now)
    comment = models.TextField()
    email = models.CharField(max_length=100)
    post_id = models.IntegerField()  
    id = models.AutoField(primary_key=True)
    # comment_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.email

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.question
