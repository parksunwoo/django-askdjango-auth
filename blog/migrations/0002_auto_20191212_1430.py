# Generated by Django 2.0.13 on 2019-12-12 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [['can_view_goldpage', 'Can view goldpage']]},
        ),
    ]