from django.http import Http404
from django.shortcuts import get_object_or_404, render

from app_employees.models import Employees

# Create your views here.
def employee_detail(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    context = {
        'employee': employee,
    }
    return render(request, 'employee_detail.html', {'employee': employee})
