# Generated by Django 3.2.12 on 2022-03-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_customer_isprojectstarted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='IsProjectStarted',
            field=models.BooleanField(default=False),
        ),
    ]
