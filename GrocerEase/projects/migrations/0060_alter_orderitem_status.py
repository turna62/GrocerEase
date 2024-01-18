# Generated by Django 4.2.6 on 2024-01-17 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0059_refund'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded')], default='Pending', max_length=20),
        ),
    ]
