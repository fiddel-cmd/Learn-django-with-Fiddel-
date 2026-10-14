
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

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


def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    form = StudentForm(request.POST or None, instance=student)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'student_form.html', {'form': form})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('home')

    return render(request, 'student_confirm_delete.html', {'student': student})


def serialize(request):
    return JsonResponse({
        "Title": "ICT-Team",
        "Issue": "NetworkIsuue",
    })