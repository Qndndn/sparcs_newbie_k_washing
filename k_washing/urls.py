from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/',views.k_washingCreate.as_view()),
    path('', views.k_washingList.as_view()),
]