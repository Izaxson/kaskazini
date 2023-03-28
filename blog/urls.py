import statistics
from django import views
from blog import views
from django.contrib import admin
from django.urls import path , include

from blogproj import settings
from .views import ContactView, HomeListView , AboutListView ,  ArticleDetailView
from django.conf.urls.static import static
from ckeditor_uploader import views as ckeditor_views
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('article/', HomeListView.as_view(), name='article'),
    path('about/', AboutListView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('article/<str:slug>', ArticleDetailView.as_view(), name='full-article'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    # path('post/int<pk>', views.post ,name="full-article"),
    # path('contact/', views.contact ,name="contact"),
    # path('', views.home ,name="home"),
    # path('about/', views.about ,name="about"),
    
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

