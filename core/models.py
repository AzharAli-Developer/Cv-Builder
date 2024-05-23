from django.db import models

# Create your models here.
class Image(models.Model):
    name=models.CharField(max_length=128)
    email=models.EmailField()
    dob=models.CharField(max_length=128)
    address=models.CharField(max_length=128)
    photo=models.ImageField(upload_to='my_images')
    doc=models.ImageField(upload_to='doc')