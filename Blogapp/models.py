from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):
    author_name = models.ForeignKey(User,null=True,default=True, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
