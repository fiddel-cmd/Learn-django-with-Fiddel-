from django import forms

from student_portal.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'registration_number', 'email', 'course')
