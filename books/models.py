from django.db import models

# Create your models here.

class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    genres=models.CharField(max_length=200)
    publisher=models.CharField(max_length=200)
    cover=models.ImageField(upload_to='images',null=True,blank=True)
    released=models.DateField(null=True,blank=True)
    about=models.CharField(max_length=200,blank=True)
    file=models.FileField(upload_to="files",null=True,blank=True)
    
    def __str__(self):
        return self.name
    


