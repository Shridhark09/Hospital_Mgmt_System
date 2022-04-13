# Generated by Django 4.0.1 on 2022-03-25 08:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_alter_patient_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Doctor',
        ),
        migrations.AddField(
            model_name='patient',
            name='Doctor_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
