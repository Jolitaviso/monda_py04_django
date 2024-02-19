from django.urls import path
from . import views

urlpatterns = [
    path('information/', views.information_list, name='information_list'),
    path('information/<int:pk>/', views.information_detail, name='information_detail'),
]
