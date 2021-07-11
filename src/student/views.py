from django.shortcuts import render, redirect

from .forms import StudentForm


def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    form = StudentForm
    context = {
        "form" : form
    }
    return render(request, 'student/student_form.html', context)
