from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from yyhs import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'classes', views.ClassesViewSet)
router.register(r'teacher', views.TeacherViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'image', views.ImageViewSet)
router.register(r'album', views.AlbumViewSet)
router.register(r'blog', views.BlogViewSet)
router.register(r'blogcomment', views.BlogCommentViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'newscomment', views.NewsCommentViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'bottle', views.BottleViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yyhsserver.views.home', name='home'),
    # url(r'^yyhsserver/', include('yyhsserver.foo.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
