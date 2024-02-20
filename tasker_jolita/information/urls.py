from django.urls import path
from . import views

urlpatterns = [
    path('', views.information_list, name='information_list'),
    path('<int:pk>/', views.information_detail, name='information_detail'),
]
