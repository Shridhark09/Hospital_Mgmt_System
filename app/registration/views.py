from urllib import request

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Patient, Doctor, Bed
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your views here.
def home(request):
    patientList = Patient.objects.all()
    count=len(patientList)
    doctorList = Doctor.objects.all()
    count_doctor=len(doctorList)
    return render(request, "home.html",{'count': count,'count_doctor':count_doctor})


def base(request):
    return render(request, "base.html")


def doctor(request):
    doctorList = Doctor.objects.all()
    count_doctor=len(doctorList)
    return render(request, "doctors.html", {'doctorList': doctorList, 'count_doctor':count_doctor})


def collect(request):
    d = Doctor()
    print("inside collect ")
    d.Doctor_name = request.POST.get('Doctor_name')
    d.Age = request.POST.get('Age')
    d.Experience = request.POST.get('Experience')
    d.Speciality = request.POST.get('Speciality')
    d.Mobile = request.POST.get('Mobile')
    d.Email = request.POST.get("Email")

    d.save()
    messages.success(request, "Doctor added Successfully! ")
    return redirect('/doctor')


def deleteDoctor(request, pk):
    d = Doctor.objects.get(id=pk)
    name = d.Doctor_name
    d.delete()
    messages.success(request, f"Doctor '{name}' deleted successfully")
    return redirect('/doctor')


def patient(request):
    patientList = Patient.objects.all()
    count=len(patientList)
    return render(request, "patient.html", {'patientList': patientList, 'count': count})


def store(request):
    p = Patient()
    p.Patient_name = request.POST.get('Patient_name')
    p.Appointment_date = request.POST.get('Appointment_date')
    p.Disease = request.POST.get('Disease')
    p.Doctor_name = request.POST.get('Doctor_name')
    p.Bed = request.POST.get('Bed')
    p.Blood_group = request.POST.get('Blood_group')
    p.Gender = request.POST.get('Gender')
    p.Phone = request.POST.get('Phone')
    p.Age = request.POST.get('Age')

    p.save()
    messages.success(request, "Appointment Booked !")
    return redirect('/')


def deletePatient(request, pk):
    p = Patient.objects.get(id=pk)
    name = p.Patient_name
    p.delete()
    messages.success(request, f"Patient '{name}' deleted successfully")
    return redirect('/patient')


def appointment(request):
    doctorList = Doctor.objects.raw('select id from registration_doctor')
    bedList=Bed.objects.raw('select id from registration_bed')
    return render(request,'appointment.html',{'doctorList': doctorList, 'bedList':bedList})


def dashboard(request):
    patientList = Patient.objects.all()
    count = len(patientList)
    doctorList = Doctor.objects.all()
    count_doctor = len(doctorList)
    count_bed=Bed.objects.all().aggregate(count_bed=Sum('bed_count'))

    return render(request, "dashboard.html", {'count': count, 'count_doctor': count_doctor,'count_bed':count_bed})




def login(request):
    return HttpResponseRedirect("/accounts/login")


class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"


def add_doctor(request):
    return render(request, "add_doctor.html")


def services(request):
    return render(request, "services.html")

def collect_Beds(request):
    b=Bed()
    b.Bed_name=request.POST.get('Bed_name')
    b.bed_count=request.POST.get('bed_count')

    b.save()
    messages.success(request, "Bed added Successfully! ")
    return redirect('/bed')

def deleteBed(request, pk):
    b = Bed.objects.get(id=pk)
    name = b.Bed_name
    b.delete()
    messages.success(request, f"Bed '{name}' deleted successfully")
    return redirect('/bed')


def bed(request):
    bedList = Bed.objects.all()
    count_bed=Bed.objects.all().aggregate(count_bed=Sum('bed_count'))
    return render(request, "beds.html", {'bedList': bedList,'count_bed':count_bed} )


def add_bed(request):
    bedList = Bed.objects.raw('select id from registration_bed')
    return render(request,'add_bed.html',{'bedList': bedList})

def updateBed(request,pk):
    bed=Bed.objects.get(id=pk)
    return render(request,'updateBed.html',{'b': bed})


def saveUpdatedBed(request,pk):
    b= Bed.objects.get(id=pk)
    b.Bed_name=request.POST.get('Bed_name')
    b.bed_count=request.POST.get('bed_count')
    print(b.Bed_name)
    print(b.bed_count)
    b.save()  #update details
    messages.success(request,f"You have updated details successfully")
    return redirect('/bed')

def search(request):
    search=request.GET['search']
    if len(search)>20:
        patientList=Patient.objects.none()
    else:
        patientList=Patient.objects.filter(Patient_name=search)

    if patientList.count()==0:
        messages.warning(request,"No search result found. Please search it again")

    return render(request,'search.html',{'patientList':patientList,'search': search})