# Generated by Django 5.1 on 2024-08-25 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_stages_date_finish_alter_stages_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letterstais',
            name='date',
            field=models.DateField(default=datetime.date(2024, 8, 25)),
        ),
    ]
