# Generated by Django 2.2.15 on 2020-08-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpage', '0015_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]
