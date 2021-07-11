from django.shortcuts import render, redirect


def index(request):
    return render(request, 'student/index.html')

