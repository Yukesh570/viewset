# Generated by Django 5.1.1 on 2024-09-18 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewSet_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detail',
            options={'ordering': ['country'], 'verbose_name': 'testdata'},
        ),
    ]
