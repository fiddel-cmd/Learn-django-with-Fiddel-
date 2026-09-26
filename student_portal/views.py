
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "student_name" :"Brian",
        "student_Course" :"BBIT"

    }
    return render (request,"home.html",context)