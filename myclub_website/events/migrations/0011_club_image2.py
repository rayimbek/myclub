# Generated by Django 4.2 on 2023-05-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_club_club_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
