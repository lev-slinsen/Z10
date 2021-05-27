# Generated by Django 3.2.2 on 2021-05-23 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20210523_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name='order date'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('choice_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.pizza')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.order')),
            ],
        ),
    ]