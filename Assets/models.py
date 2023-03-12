from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Companies'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.first_name + self.user.last_name
    
class deviceType(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()


class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.CharField(max_length=255)
    checked_out = models.BooleanField(default=False)
    checked_out_date = models.DateTimeField(null=True)
    checked_in_date = models.DateTimeField(null=True)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, related_name='checked_out_devices')
    checked_in_by = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, related_name='checked_in_devices')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} @{self.company.name}'

    @property
    def date_diff(self):
        return (self.checked_out_date - self.checked_in_date).days

