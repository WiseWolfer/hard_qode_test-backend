# Generated by Django 4.2.10 on 2024-08-20 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_subscription_what_a_course'),
        ('courses', '0005_remove_lesson_crs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='What_a_Course',
        ),
        migrations.AddField(
            model_name='course',
            name='What_a_sub',
            field=models.ForeignKey(choices=[], null=True, on_delete=django.db.models.deletion.CASCADE, to='users.subscription', verbose_name='Какая подписка'),
        ),
    ]
