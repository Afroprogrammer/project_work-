# Generated by Django 2.0.8 on 2018-11-14 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shitty', '0007_dislodgedates_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='initial_dislodge',
            field=models.DateField(blank=True, null=True),
        ),
    ]