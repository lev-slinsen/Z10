from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
