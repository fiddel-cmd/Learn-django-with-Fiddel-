
from django.shortcuts import render

from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.order_by('name')
    return render(request, "home.html", {"students": students})