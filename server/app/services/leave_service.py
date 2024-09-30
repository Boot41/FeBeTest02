from django.shortcuts import get_object_or_404
from .models import LeaveBalance
from rest_framework.response import Response
from rest_framework import status

# Logic for requesting leave

def request_leave(employee_id, leave_type, days):
    leave_balance = get_object_or_404(LeaveBalance, employee_id=employee_id, leave_type=leave_type)
    if leave_balance.balance >= days:
        leave_balance.balance -= days
        leave_balance.save()
        return Response({'message': 'Leave requested successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Insufficient leave balance.'}, status=status.HTTP_400_BAD_REQUEST)

# Additional code can go here if needed.