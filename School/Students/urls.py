from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('courses/', views.courses),
    path('about/', views.about),
    path('contact/', views.contact),
    path('students/', views.students),
    path('schools/', views.schools),
    path('teachers/', views.teachers),
    path('insert_students/', views.insert_students)

]