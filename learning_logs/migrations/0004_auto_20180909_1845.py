# Generated by Django 2.1.1 on 2018-09-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topics_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
