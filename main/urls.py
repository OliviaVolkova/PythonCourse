from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('authorization', views.authorization),
    path('userpage', views.userpage)

]