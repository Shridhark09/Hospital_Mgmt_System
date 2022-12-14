# Generated by Django 4.0.1 on 2022-03-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Date_of_Appointment', models.DateTimeField()),
                ('Reason', models.CharField(max_length=20)),
                ('Beds', models.CharField(max_length=20)),
                ('Blood_group', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=20)),
                ('Phone_No', models.CharField(max_length=20)),
                ('Age', models.PositiveSmallIntegerField()),
                ('Message', models.TextField()),
            ],
        ),
    ]
