# Generated by Django 2.1.7 on 2019-03-04 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catdata',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='catdata',
            name='longitude',
        ),
    ]
