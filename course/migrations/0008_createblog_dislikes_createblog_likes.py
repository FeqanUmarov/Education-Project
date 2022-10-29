# Generated by Django 4.1.1 on 2022-10-29 14:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0007_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='createblog',
            name='dislikes',
            field=models.ManyToManyField(blank=True, null=True, related_name='disliked_blogs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='createblog',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
