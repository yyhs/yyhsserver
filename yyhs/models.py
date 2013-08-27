from django.db import models
from django.contrib.auth.models import User,Group

VISIABLE_CHOICES = [("all","all"), ("class","class"), ("personal","personal")]
SEX_CHOICES = [("male", "male"), ("female","female")]

class UserInfo(models.Model):
    user = models.OneToOneField(User,primary_key=True)
    age = models.IntegerField()
    sex = models.CharField(choices=SEX_CHOICES, default="male", max_length=6)
    mobilephone = models.IntegerField(max_length=13)
    face = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Teacher(UserInfo):
    subject = models.CharField(max_length=20)

class Classes(models.Model):
    name = models.CharField(max_length=10)
    year = models.DateField()
    number = models.IntegerField()
    head_teacher = models.OneToOneField(Teacher)
    logo = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher,related_name="%(app_label)s_%(class)s_related")

    def __unicode__(self):
        return u"classname is %s" % self.name

class Student(UserInfo):
    banji = models.ForeignKey(Classes)

class Album(models.Model):
    name = models.CharField(max_length=100, blank=True, default="album name")
    author = models.CharField(max_length=100)
    pubdate = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, blank=True, default="")
    visiable = models.CharField(choices=VISIABLE_CHOICES,default="all",max_length=10)

    class Meta:
        ordering = ('pubdate',)

class Image(models.Model):
    album = models.ForeignKey(Album)
    name = models.CharField(max_length=100)
    pubdate = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100)

    class Meta:
        ordering = ('pubdate',)

class Post(models.Model):
    author = models.ForeignKey(User)
    content = models.CharField(max_length=1024)
    pubdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class News(Post):
    title = models.CharField(max_length=100)

class Blog(Post):
    tag = models.CharField(max_length=10)
    belong_class = models.IntegerField()

class Notes(Post):
    target = models.CharField(max_length=10)
    anonymous = models.IntegerField()

#class Comment(Post):
#    post = models.ForeignKey(Post)

