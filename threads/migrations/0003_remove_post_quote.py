# Generated by Django 2.2.2 on 2019-06-26 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_auto_20190626_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='quote',
        ),
    ]
