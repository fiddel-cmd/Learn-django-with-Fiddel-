from django.contrib import admin

# Register your models here.
from django.urls import include, path

urlpatterns =  [

    path('admin/',admin.site.urls),
    path('',include('student_portal.urls'))
]