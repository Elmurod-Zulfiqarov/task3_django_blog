from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Comment(models.Model):
    content = models.CharField(max_length=2048)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    sub_content = models.CharField(max_length=512)
    image = models.ImageField(upload_to="media/post")

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
