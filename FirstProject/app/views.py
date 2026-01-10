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
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        comments = request.POST.get('comments')
        print(FirstName, LastName, email, password,
              address, city, state, zip, comments)

        Customer.objects.create(
            FirstName=FirstName,
            LastName=LastName,
            email=email,
            password=password,
            address=address,
            city=city,
            state=state,
            zip=zip,
            comments=comments
        )
        return redirect('show')  # Redirect to home page after successful submission
    return render(request, 'register.html')