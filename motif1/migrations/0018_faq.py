# Generated by Django 5.0.1 on 2024-03-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motif1', '0017_comment_post_id_alter_blogpost_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]