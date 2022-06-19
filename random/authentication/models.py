from django.db import models

# Create your models here.
class Loginform(models.Model):
    username= models.CharField(max_length=50)
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=200)
    email= models.EmailField()
    phone = models.IntegerField()
