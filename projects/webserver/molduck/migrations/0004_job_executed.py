# Generated by Django 5.0.7 on 2024-07-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molduck', '0003_remove_job_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='executed',
            field=models.BooleanField(default=False),
        ),
    ]
