# Generated by Django 3.0.8 on 2020-08-03 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_carmodels_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodels',
            name='price',
            field=models.CharField(default='starting at ₹lakhs', max_length=150),
        ),
    ]
