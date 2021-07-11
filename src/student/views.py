from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Student



def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():

            student_name = form.cleaned_data.get("first_name")
            student_surname = form.cleaned_data.get("last_name")
            student_number = form.cleaned_data.get("number")

            print('student saved successfully')
            print(student_name, student_surname, student_number)
            return redirect('index') # bilgileri geri göndermek için(form valid değilse)
        context = {
            'form': form
        }
        return render(request, 'student/student_form.html', context)
    # GET methodu ise doğrudan burası calısacak.
    form = StudentForm
    context = {
        "form" : form
    }
    return render(request, 'student/student_form.html', context)
