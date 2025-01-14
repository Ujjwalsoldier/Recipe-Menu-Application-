# home/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    # import pdb ; pdb.set_trace() -- this is just for debuging
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'address', 'image', 'file']
