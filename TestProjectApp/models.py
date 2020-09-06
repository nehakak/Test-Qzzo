from django.db import models

class Project(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    Age = models.IntegerField()
    Image= models.ImageField(upload_to='test/images/')
    LoginID = models.CharField(max_length=200,unique=True )
    EmailID = models.CharField(max_length=500,unique=True )
    Password = models.CharField(max_length=50)
