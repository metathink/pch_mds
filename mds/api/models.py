from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    tag = models.CharField(max_length=30)
    tool = models.CharField(max_length=30)

    def __str__(self):
        return self.title
