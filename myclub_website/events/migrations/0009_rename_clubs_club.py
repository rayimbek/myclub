# Generated by Django 4.2 on 2023-05-26 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_subject_timeremaining_clubs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clubs',
            new_name='Club',
        ),
    ]