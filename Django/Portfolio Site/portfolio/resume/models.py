from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    email=models.EmailField()
    phone=models.CharField(max_length=15)

class Experience(models.Model):
    company=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField(null=True,blank=True)
    description=models.TextField()

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    technologies=models.CharField(max_length=200)
    link=models.URLField(blank=True,null=True)


