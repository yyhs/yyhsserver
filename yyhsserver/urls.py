from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from yyhs import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'userinfo', views.UserInfoViewSet)
router.register(r'classes', views.ClassesViewSet)
router.register(r'image', views.ImageViewSet)
router.register(r'album', views.AlbumViewSet)
router.register(r'post', views.PostViewSet)
router.register(r'comment', views.CommentViewSet)

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
