# Generated by Django 5.0.1 on 2024-03-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motif1', '0008_remove_team_id_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='id_user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]