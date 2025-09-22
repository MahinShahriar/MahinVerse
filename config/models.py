from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # skills =
    image = models.ImageField(upload_to='projects')
    description = models.TextField()
    source_code = models.URLField(default='')

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(unique=True)
    img = models.ImageField(upload_to='blog', null=True)
    category = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
