# Generated by Django 3.1.5 on 2021-01-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpage', '0026_auto_20200823_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='function',
            field=models.IntegerField(choices=[(0, 'Talks'), (1, 'Discussions')], default=0),
        ),
    ]