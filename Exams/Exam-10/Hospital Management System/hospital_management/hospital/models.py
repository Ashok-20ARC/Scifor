from django.db import models

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=[('male','Male'),('female','Female')])
    phone=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    address=models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    status=models.CharField(max_length=20,choices=[('Pending','pending'),('Completed','completed')])

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
    
class Billing(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=20,choices=[('unpaid','Unpaid'),('paid','Paid')])

    def __str__(self):
        return f"Bill for {self.patient.name} - Rs.{self.total_amount}"