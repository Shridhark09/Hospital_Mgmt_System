# Generated by Django 4.0.1 on 2022-03-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Speciality', models.CharField(max_length=20)),
                ('Phone_No', models.CharField(max_length=20)),
                ('Age', models.PositiveSmallIntegerField()),
                ('Experience', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Message',
        ),
    ]