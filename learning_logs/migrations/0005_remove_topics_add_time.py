# Generated by Django 2.1.1 on 2018-09-09 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_auto_20180909_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='add_time',
        ),
    ]