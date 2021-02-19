# Generated by Django 3.1.5 on 2021-02-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_auto_20210219_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('1', 'Open'), ('2', 'Work in Progress'), ('3', 'Complete'), ('4', 'Closed'), ('5', 'Canceled')], default='1', max_length=50, verbose_name='Status'),
        ),
    ]
