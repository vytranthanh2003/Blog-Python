from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(null=True)
    audio =  models.FileField(upload_to='music', null = True)
    
    def __str__(self):
        return self.title