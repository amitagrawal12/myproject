from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'post_images')
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(to=Post,on_delete=CASCADE,related_name='posts')
    description = models.TextField()
    
    def __str__(self):
        return self.description








