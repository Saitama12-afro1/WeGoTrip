# Generated by Django 4.2.6 on 2023-10-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_status_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
