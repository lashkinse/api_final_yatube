# Generated by Django 3.2.16 on 2022-12-29 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221229_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='created',
        ),
    ]
