# Generated by Django 2.1.7 on 2019-03-04 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0003_auto_20190304_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='center.Cat'),
        ),
    ]