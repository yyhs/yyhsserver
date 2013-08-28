from django.contrib.auth.models import User,Group
from rest_framework import serializers
from yyhs.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ClassesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classes
        fields = ('name','graduate','head_teacher')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('name','pubdate','url')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('name','author','pubdate')

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News

class NewsCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsComment

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog

class BlogCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogComment

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message

class BottleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bottle
