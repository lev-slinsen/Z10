from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_pizza_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.size'),
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='pizza',
            name='ingredients',
            field=models.ManyToManyField(to='stock.Ingredient'),
        ),
    ]
