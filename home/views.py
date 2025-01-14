from django.shortcuts import render ,redirect
from django.http import HttpResponse
from home.forms import StudentForm 
# Forms project


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  # handle file uploads as well
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page after saving the data
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})


# success_page
def success_page(request):
    return render(request, 'success.html') 


# Create your views here.

def home(request):

    peoples =[
        {'name' : 'Ujjwal Aditya' , 'age' : 25 },
        {'name' : 'Aprajita Aditya' , 'age' : 16 },
        {'name' : 'kullu kumar' , 'age' : 24 },
        {'name' : 'Rohan Raj' , 'age' : 10 },
        {'name' : 'Deepak Kumar' , 'age' : 27 },

    ]

    vegetables = [ 'pumpkin','tomato','potato']

    for people in peoples :
        print(people)

    return render(request , "index.html" , context = { 'page' : 'Django 2024 Tutorials ' , 'peoples' : peoples , 'vegetables' : vegetables }) 

def about (request):
    context = {'page' : 'about' }
    return render(request , "about.html" , context ,)
    

def contact (request):
    context = {'page' : 'contact' }
    return render(request , "contact.html" , context)

def success_pagee(request):
    print("*" *10)


    return HttpResponse("""<h1>Hey this is a success page<h1>
        <p> Hey this is coming from django server </p>
        <hr>
        <h3 style="color:red"> i'm loving this projoect:) </h3>
    
    """)
