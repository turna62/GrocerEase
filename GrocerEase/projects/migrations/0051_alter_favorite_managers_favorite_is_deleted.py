# Generated by Django 4.2.5 on 2024-01-14 14:27

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0050_alter_notification_managers_notification_is_deleted'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='favorite',
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='favorite',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
