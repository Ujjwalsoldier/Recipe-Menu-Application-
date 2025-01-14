from django.contrib import admin

# Register your models here.

from home.models import Student, Product , Car 

# Register your models
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Car)

