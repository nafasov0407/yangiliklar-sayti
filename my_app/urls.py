from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',indexPage,name = 'index'),
	path('post_detail/<str:nevs_id>/',post_detailPage,name = 'post_detail'),
	path('foother/<int:category_id>/',footherPage,name = 'foother'),
	] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)