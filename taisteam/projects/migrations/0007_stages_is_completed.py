# Generated by Django 5.0.7 on 2024-08-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_stages_date_finish_alter_stages_date_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='stages',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
