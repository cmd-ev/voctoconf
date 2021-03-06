# Generated by Django 2.2.15 on 2020-08-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbb', '0003_roomstats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomstats',
            name='attendees',
        ),
        migrations.AddField(
            model_name='roomstats',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roomstats',
            name='listeners',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roomstats',
            name='participants',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roomstats',
            name='recording',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='roomstats',
            name='videocount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roomstats',
            name='voiceparticipants',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roomstats',
            name='moderators',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roomstats',
            name='presenter',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
