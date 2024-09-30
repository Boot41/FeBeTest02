from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Employee


def get_organization_directory():
    employees = Employee.objects.all().values('employee_id', 'name')
    return JsonResponse(list(employees), safe=False)


def get_organization_structure():
    # Logic to fetch the hierarchical structure of the organization goes here.
    # This would typically require a model field or a related model to establish hierarchy
    organization_structure = []  # Placeholder for structure data
    return JsonResponse(organization_structure, safe=False)
