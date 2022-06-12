from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='myschapp-home'),
    path('about/', views.about, name='myschapp-about'),
]