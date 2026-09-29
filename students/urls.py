from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='student-list'),
    path('create/', views.create_student, name='student-create'),
]