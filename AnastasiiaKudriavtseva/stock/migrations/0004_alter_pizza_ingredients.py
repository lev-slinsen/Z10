from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20210523_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='ingredients',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.ingredient'),
        ),
    ]
