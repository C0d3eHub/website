from django.db import models
from django.utils import timezone
#headermodel

from django.db import models

#header model

class HeaderContent(models.Model):
    logo = models.ImageField(upload_to='logos/')
    h1 = models.CharField(max_length=200)
    h2 = models.CharField(max_length=200)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    paragraph3 = models.TextField()
    button1_text = models.CharField(max_length=100)
    button1_url = models.CharField(max_length=200)
    button2_text = models.CharField(max_length=100)
    button2_url = models.CharField(max_length=200)

    def __str__(self):
        return self.h1



class NewsAlert(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(default=timezone.now)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return self.title


class PrincipalDesk(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='principal_images/', blank=True, null=True)  # New field for image

    def __str__(self):
        return self.title


class AboutInstitute(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Auto update on save

    def __str__(self):
        return self.title


class AdminStaff(models.Model):
    serial_number = models.AutoField(primary_key=True)  # Explicit primary key
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)  # Ensure Pillow is installed

    def __str__(self):
        return self.name
class MyModel(models.Model):
    # Define your fields here
    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=255)  # Make sure these fields exist in models.py
    field3 = models.DateField()

    def __str__(self):
        return self.field1
class TechStaff(models.Model):
    serial_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='techstaff_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or f'Image {self.id}'