# Generated by Django 3.1.5 on 2021-02-19 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20210219_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='STB_Number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.stb'),
        ),
    ]
