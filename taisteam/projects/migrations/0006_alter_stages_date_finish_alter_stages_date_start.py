# Generated by Django 5.0.7 on 2024-08-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_stages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stages',
            name='date_finish',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='stages',
            name='date_start',
            field=models.DateField(null=True),
        ),
    ]
