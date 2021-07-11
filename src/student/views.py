from django.shortcuts import render, redirect


def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    return render(request, 'student/student_form.html')
