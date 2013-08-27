from django.db import models

VISIABLE_CHOICES = [("all","all"), ("class","class"), ("personal","personal")]
SEX_CHOICES = [("male", "male"), ("female","female")]

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(choices=SEX_CHOICES, default="male", max_length=6)
    email = models.EmailField(max_length=75)
    mobilephone = models.IntegerField(max_length=13)
    face = models.CharField(max_length=100)
    jointime = models.DateTimeField(auto_now_add=True)
    industry = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)

class classes(models.Model):
    graduate = models.DateField()
    head_teacher = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Image(models.Model):
    name = models.CharField(max_length=100)
    pubdate = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100)

    class Meta:
        ordering = ('pubdate',)

class Album(models.Model):
    name = models.CharField(max_length=100, blank=True, default="album name")
    author = models.CharField(max_length=100)
    pubdate = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, blank=True, default="")
    visiable = models.CharField(choices=VISIABLE_CHOICES,default="all",max_length=10)

    class Meta:
        ordering = ('pubdate',)

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=1024)
    category = models.CharField(max_length=10)
    pubdate = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    reference = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pubdate = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1024)
