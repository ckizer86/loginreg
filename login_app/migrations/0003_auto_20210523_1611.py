# Generated by Django 2.2 on 2021-05-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20210523_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(),
        ),
    ]