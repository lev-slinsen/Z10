# Generated by Django 3.2.2 on 2021-05-24 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20210513_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.pizza')),
            ],
        ),
    ]