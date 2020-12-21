from django.urls import path
from . import views

# setting up the homepage mapping. 
urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about')
]
