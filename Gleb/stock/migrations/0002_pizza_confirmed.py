# Generated by Django 3.2.2 on 2021-05-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
