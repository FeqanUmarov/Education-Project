# Generated by Django 4.1.1 on 2022-10-17 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='answercourse',
            field=models.CharField(max_length=200),
        ),
    ]
