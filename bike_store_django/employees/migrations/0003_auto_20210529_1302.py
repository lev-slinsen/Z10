# Generated by Django 3.2.3 on 2021-05-29 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20210529_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='manager',
        ),
        migrations.AddField(
            model_name='timetable',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incharge', to='employees.employee'),
        ),
    ]
