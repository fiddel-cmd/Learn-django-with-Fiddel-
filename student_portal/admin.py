from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "registration_number", "email", "course")
    search_fields = ("name", "registration_number", "email", "course")