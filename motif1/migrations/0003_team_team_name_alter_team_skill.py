# Generated by Django 5.0.1 on 2024-03-06 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motif1', '0002_alter_team_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='skill',
            field=models.TextField(),
        ),
    ]