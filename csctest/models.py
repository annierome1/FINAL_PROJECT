#######################
#####
##### Models for admin page
#####
#######################

#imports needed functions
from django.db import models
from ckeditor.fields import RichTextField

#exhbits class that allows for title, content, and image to be uploaded 
class Exhibit(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    additional_content = models.TextField(blank=True, null=True) 
    image = models.ImageField(upload_to='html_pages_images/', blank=True, null=True)

    def __str__(self):
        return self.title

#email class that allows email submisson
class Email(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"Feedback from {self.name}"