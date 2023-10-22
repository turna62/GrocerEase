# Generated by Django 4.2.6 on 2023-10-22 05:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_merge_20231022_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.customer')),
            ],
        ),
    ]
