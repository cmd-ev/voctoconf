# Generated by Django 3.1.5 on 2021-01-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authstuff', '0004_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
