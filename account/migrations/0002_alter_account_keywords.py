# Generated by Django 3.2.5 on 2021-07-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='keywords',
            field=models.TextField(default='', max_length=100),
        ),
    ]
