from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course, Customer

# Create your views here.


# def show(request):
#     return HttpResponse("Hello World")

def home(request):
    course_data = Course.objects.all()
    customer_data = Customer.objects.all()
    return render(request, 'home.html', {'a': course_data, 'b': customer_data})                     #render le templates ko file laii browser samma load garne kaam ho
    
#object ko name a deko ho here


def form(request):
    if request.method == "POST":
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        email = request.POST.get('Email')  # Changed: 'email' -> 'Email'
        password = request.POST.get('Password')  # Changed: 'password' -> 'Password'
        comments = request.POST.get('Comments')  # Changed: 'comments' -> 'Comments'
        print(FirstName, LastName, email, password, comments)

        Customer.objects.create(
            FirstName=FirstName,
            LastName=LastName,
            email=email,
            password=password,
            comments=comments
        )
        return redirect('form')  # Redirect to home page after successful submission
    return render(request, 'register.html')