# Generated by Django 4.1.1 on 2022-09-23 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_coursephoto_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursephoto',
            name='branch',
        ),
    ]