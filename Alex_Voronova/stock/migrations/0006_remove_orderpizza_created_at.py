# Generated by Django 3.2.2 on 2021-05-26 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_orderpizza_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpizza',
            name='created_at',
        ),
    ]
