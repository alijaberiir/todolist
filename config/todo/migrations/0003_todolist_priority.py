# Generated by Django 3.2.8 on 2021-10-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todolist_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='priority',
            field=models.CharField(choices=[(0, 'هیچ'), (1, 'سبز'), (2, 'زرد'), (3, 'نارنجی'), (4, 'قرمز')], default=0, max_length=10, verbose_name='اولویت'),
        ),
    ]