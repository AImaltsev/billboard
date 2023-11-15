from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code_registration = models.CharField(max_length=100)

class Category(models.Model):
    title = models.CharField(max_length=100)


class Ad(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    choices = models.BooleanField()
    views = models.IntegerField()

class AdCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class News(models.Model):
    title = models.CharField(max_length=100)
    text = HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class LikePage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


