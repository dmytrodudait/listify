# Generated by Django 4.0.4 on 2022-07-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listify',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
