# Generated by Django 5.0.1 on 2024-03-06 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motif1', '0003_team_team_name_alter_team_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='user',
        ),
    ]