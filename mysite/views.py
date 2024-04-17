from django.shortcuts import render
from app_employees.models import Employees

def home(request):
    employees = Employees.objects.all()
    context = {
        'employees': employees,
    }
    # Add your logic here
    return render(request, 'home.html', context)