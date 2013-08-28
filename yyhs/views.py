from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from yyhs.serializers import *
from yyhs.models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ClassesViewSet(viewsets.ModelViewSet):

    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class TeacherViewSet(viewsets.ModelViewSet):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ImageViewSet(viewsets.ModelViewSet):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class NewsViewSet(viewsets.ModelViewSet):

    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsCommentViewSet(viewsets.ModelViewSet):

    queryset = NewsComment.objects.all()
    serializer_class = NewsCommentSerializer

class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogCommentViewSet(viewsets.ModelViewSet):

    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class BottleViewSet(viewsets.ModelViewSet):

    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer
