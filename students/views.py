from django.shortcuts import redirect, render

from student_portal.models import Student

from .forms import StudentForm


def home(request):
	students = Student.objects.order_by('name')
	return render(request, 'home.html', {'students': students})


def create_student(request):
	form = StudentForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('student-list')

	return render(request, 'student_form.html', {'form': form})
