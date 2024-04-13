# Generated by Django 5.0.1 on 2024-03-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motif1', '0011_alter_team_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
