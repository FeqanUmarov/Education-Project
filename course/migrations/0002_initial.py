# Generated by Django 4.1.1 on 2022-10-12 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainerapply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainer',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.location'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lessonplan',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.courseboss'),
        ),
        migrations.AddField(
            model_name='lessonplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examapply',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.courseboss'),
        ),
        migrations.AddField(
            model_name='examapply',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.exam'),
        ),
        migrations.AddField(
            model_name='exam',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.branchs'),
        ),
        migrations.AddField(
            model_name='exam',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.courseboss'),
        ),
        migrations.AddField(
            model_name='eventapply',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.event'),
        ),
        migrations.AddField(
            model_name='eventapply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.trainer'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coursephoto',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.courseboss'),
        ),
        migrations.AddField(
            model_name='courseboss',
            name='course_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursetype'),
        ),
        migrations.AddField(
            model_name='courseboss',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courseapply',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.courseboss'),
        ),
        migrations.AddField(
            model_name='courseapply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='course.courseboss', verbose_name='Kurs'),
        ),
        migrations.AddField(
            model_name='branchs',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.courseboss'),
        ),
    ]
