# Generated by Django 3.2.5 on 2021-07-31 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='hire_data',
            new_name='hire_date',
        ),
    ]