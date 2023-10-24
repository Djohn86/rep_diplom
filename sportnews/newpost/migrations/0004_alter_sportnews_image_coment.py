# Generated by Django 4.2.5 on 2023-10-23 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newpost', '0003_alter_sportnews_tsport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportnews',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Up vote'), ('down', 'Down vote')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newpost.sportnews')),
            ],
            options={
                'unique_together': {('owner', 'post')},
            },
        ),
    ]
