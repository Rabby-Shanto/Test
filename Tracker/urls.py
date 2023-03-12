from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from Assets import views

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'device', views.DeviceViewSet,basename="device")
router.register(r'company', views.CompanyViewSet,basename="company")
router.register(r'employee', views.EmployeeViewSet,basename="employee")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]