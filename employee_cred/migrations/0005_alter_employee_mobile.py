# Generated by Django 4.2 on 2023-05-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_cred', '0004_rename_titile_position_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
