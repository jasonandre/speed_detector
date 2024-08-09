from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.speed_detector, name='speed_detector')]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)