from django.shortcuts import render

from student_portal.models import Student


def home(request):
	students = Student.objects.order_by('name')
	return render(request, 'home.html', {'students': students})
