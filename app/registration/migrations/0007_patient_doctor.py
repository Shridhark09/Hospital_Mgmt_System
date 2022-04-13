# Generated by Django 4.0.1 on 2022-03-25 06:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_doctor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.doctor'),
            preserve_default=False,
        ),
    ]