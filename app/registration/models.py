from django.db import models


# Create your models here.
class Patient(models.Model):
    # doctor=models.ForeignKey('Doctor',on_delete=models.CASCADE)
    Patient_name = models.CharField(max_length=20)
    Appointment_date = models.DateField()
    Disease = models.CharField(max_length=20)
    Doctor_name=models.CharField(max_length=20)
    Bed = models.CharField(max_length=20)
    Blood_group = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Age = models.PositiveSmallIntegerField()


class Doctor(models.Model):
    Doctor_name = models.CharField(max_length=20)
    Age = models.PositiveSmallIntegerField()
    Experience = models.PositiveSmallIntegerField()
    Speciality = models.CharField(max_length=20)
    Mobile = models.CharField(max_length=20)
    Email = models.EmailField()

class Bed(models.Model):
    Bed_name= models.CharField(max_length=20)
    bed_count=models.PositiveSmallIntegerField()


