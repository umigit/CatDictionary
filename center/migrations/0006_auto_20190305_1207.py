# Generated by Django 2.1.7 on 2019-03-05 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0005_auto_20190304_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_original',
        ),
        migrations.AlterField(
            model_name='image',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image', to='center.Cat'),
        ),
    ]
