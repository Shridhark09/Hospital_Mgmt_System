from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('base/', views.base, name="base"),
    path('doctor/', views.doctor, name="doctor"),
    path('collect/', views.collect, name="collect"),
    path('patient/', views.patient, name="patient"),
    path('add_doctor/', views.add_doctor, name="add_doctor"),
    path('store/', views.store, name="store"),
    path('deletePatient/<int:pk>', views.deletePatient, name="deletePatient"),
    path('deleteDoctor/<int:pk>', views.deleteDoctor, name="deleteDoctor"),
    path('appointment/', views.appointment, name="appointment"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.login, name="login"),
    path('register/', views.Register.as_view(), name='register'),
    path('services/', views.services, name="services"),
    path('bed/', views.bed, name="bed"),
    path('deleteBed/<int:pk>', views.deleteBed, name="deleteBed"),
    path('add_bed', views.add_bed, name="add_bed"),
    path('updateBed/<int:pk>', views.updateBed, name="updateBed"),
    path('saveUpdatedBed/<int:pk>', views.saveUpdatedBed, name="saveUpdatedBed"),
    path('collect_Beds/', views.collect_Beds, name="collect_Beds"),
    path('search/',views.search,name="search"),

]
