# Generated by Django 5.0 on 2024-02-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_information_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='youtube_video',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Youtube video'),
        ),
    ]
