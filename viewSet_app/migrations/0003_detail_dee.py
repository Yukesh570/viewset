# Generated by Django 5.1.1 on 2024-09-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewSet_app', '0002_alter_detail_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='dee',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
