from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search_news', views.search_news, name='search_news'),
    path('home', views.home, name='home')
]
