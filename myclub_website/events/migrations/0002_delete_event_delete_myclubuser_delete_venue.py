# Generated by Django 4.2 on 2023-05-01 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='MyClubUser',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
