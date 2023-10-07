# Generated by Django 4.2.5 on 2023-10-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newpost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportnews',
            name='tsport',
            field=models.PositiveSmallIntegerField(choices=[(1, 'футбол'), (2, 'хоккей'), (2, 'баскетбол'), (2, 'теннис'), (2, 'волейбол'), (2, 'бокс')], default=1, verbose_name='tsport'),
            preserve_default=False,
        ),
    ]