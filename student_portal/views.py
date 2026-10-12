
from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.order_by('name')
    return render(request, "home.html", {"students": students})


def create_student(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'student_form.html', {'form': form})