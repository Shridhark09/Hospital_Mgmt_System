# Generated by Django 4.0.1 on 2022-03-25 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_patient_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Email',
        ),
    ]