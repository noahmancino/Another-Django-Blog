from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.title}\ndate: {self.date_posted}\nauthor: {self.author}'