from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length= 255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')       


class Post(models.Model):
    title = models.CharField(max_length= 255)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    body =  RichTextField(blank = True, null = True, max_length= 7000)
    post_date = models.DateField(auto_now_add= True)
    category = models.CharField(max_length= 255, default = 'China')
    snipped = models.CharField(max_length= 255)
 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')    



# Create your models here.
