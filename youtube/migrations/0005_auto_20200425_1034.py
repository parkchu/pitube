# Generated by Django 3.0.5 on 2020-04-25 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('youtube', '0004_video_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='good',
            field=models.ManyToManyField(default=None, related_name='good', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='whether',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('channel_photo', models.ImageField(null=True, upload_to='')),
                ('whether', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subscribe', models.ManyToManyField(related_name='subscribe', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='youtube.Channel'),
        ),
    ]
