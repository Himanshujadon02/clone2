from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    number = models.IntegerField() 
    message = models.CharField(max_length=70)

class Popular_blogs(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True) 
    content=models.TextField()
    image = models.ImageField(upload_to = "cloneApp/images",default="")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Why_netcore(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    image = models.ImageField(upload_to = "cloneApp/images",default="")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class About(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()

    video= models.FileField(upload_to = "cloneApp/images",default="")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Our_involvement(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    video= models.FileField(upload_to = "cloneApp/images",default="")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Testonomial(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    content=models.TextField()
    image = models.ImageField(upload_to = "cloneApp/images",default="")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Logo(models.Model):
    title=models.CharField(max_length=50)
    image = models.ImageField(upload_to = "cloneApp/images",default="")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# class Landing(models.Model):
#     title=models.CharField(max_length=50)
#     subtitle=models.CharField(max_length=50)
#     content=models.TextField()
#     video = models.FileField(upload_to='cloneApp/images',default="")
#     created_at=models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title