from django.contrib import admin

# Register your models here.

from .models import Student
admin.site.register(Student)



from .models import Course
admin.site.register(Course)


from .models import Customer
admin.site.register(Customer)