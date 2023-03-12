from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Device,Company,Employee,deviceType
from .serializers import DeviceSerializer,CompanySerializer,EmployeeSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Device.objects.all()
        else:
            return Device.objects.filter(company__employee__user=user)


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Company.objects.all()
        else:
            return Company.objects.prefetch_related('employee_set').all()
        

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Employee.objects.all()
        else:
            return Employee.objects.filter(user=user)