# Generated by Django 3.0.8 on 2020-08-01 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_carmodels_index_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodels',
            name='rating_car',
            field=models.CharField(default='null', max_length=150),
        ),
    ]
