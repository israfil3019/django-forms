from django import forms

from .models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50, label='Your Name')
#     last_name = forms.CharField(max_length=100, label='Last Name')
#     number = forms.IntegerField(required=False)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'number']
        labels = {"first_name": 'Adınız'}

    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        number = self.cleaned_data.get("number")

        # print(number, type(number))

        if not number == None and not 1000 < int(number) < 10000:
            raise forms.ValidationError(
                "Numbers should be between 1000 and 10000")

        values = {
            "first_name": first_name,
            "last_name": last_name,
            "number": number
        }
        return values
