# Generated by Django 4.2.5 on 2023-10-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newpost', '0004_alter_sportnews_image_coment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportnews',
            name='memo',
        ),
        migrations.AddField(
            model_name='sportnews',
            name='vote_ratio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sportnews',
            name='vote_total',
            field=models.IntegerField(default=0),
        ),
    ]