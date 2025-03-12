from django.shortcuts import render,get_object_or_404
from .models import Doctor,Patient,Appointment,Billing

# Create your views here.

def home(request):
    return render(request,'hospital/home.html')

def doctor_list(request):
    doctors=Doctor.objects.all()
    return render(request,'hospital/doctors.html',{'doctors':doctors})

def patient_list(request):
    patients=Patient.objects.all()
    return render(request,'hospital/patients.html',{'patients':patients})

def appointment_list(request):
    appointments=Appointment.objects.all()
    return render(request,'hospital/appointments.html',{'appointments':appointments})

def billing_list(request):
    billings=Billing.objects.all()
    return render(request,'hospital/billings.html',{'billings':billings})
