from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.k_washingList.as_view(), name='k_washingList'),
    path('create/',views.k_washingCreate.as_view()),
]