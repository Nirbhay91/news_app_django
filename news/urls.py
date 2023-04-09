from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsForm, name='news'),
]
