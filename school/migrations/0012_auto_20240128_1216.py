# Generated by Django 3.0.5 on 2024-01-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='cl',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('Choose One', 'Choose One'), ('Computer Science', 'Computer Science'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Information Technology', 'Information Technology')], default='Choose One', max_length=100),
        ),
    ]
