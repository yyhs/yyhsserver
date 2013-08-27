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

class UserInfoViewSet(viewsets.ModelViewSet):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class ClassesViewSet(viewsets.ModelViewSet):

    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class ImageViewSet(viewsets.ModelViewSet):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
