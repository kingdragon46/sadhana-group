# Generated by Django 3.1.5 on 2021-02-20 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_auto_20210220_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('Emp_Number', models.CharField(max_length=10, null=True, verbose_name='Employee Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('department', models.CharField(max_length=100, null=True, verbose_name='Department')),
                ('DOJ', models.DateField(verbose_name='Date of Joining')),
            ],
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='allotment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.employee'),
        ),
    ]
