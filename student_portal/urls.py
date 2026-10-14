from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_student, name="student-create"),
    path("edit/<int:student_id>/", views.update_student, name="student-edit"),
    path("delete/<int:student_id>/", views.delete_student, name="student-delete"),
    path("serialize/", views.serialize, name="serialize"),
]