from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('gallery/', views.gallery),
    path('products/', views.products)


]