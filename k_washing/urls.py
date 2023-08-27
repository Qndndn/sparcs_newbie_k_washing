from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'k_washing'

urlpatterns = [
    path('', views.k_washingList.as_view(), name='k_washingList'),
    path('delete/<int:pk_1>/<int:pk_2>/', views.k_washing_list_delete, name='k_washing_list_delete'),
    path('create/',views.k_washingCreate.as_view()),
]