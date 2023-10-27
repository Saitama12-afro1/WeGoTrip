# Generated by Django 4.2.6 on 2023-10-27 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_order_date_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='app.order'),
        ),
    ]
