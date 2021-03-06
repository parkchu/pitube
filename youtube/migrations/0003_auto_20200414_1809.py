# Generated by Django 3.0.5 on 2020-04-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_video_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(help_text='썸네일 사진을 첨부해주세요', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(help_text='동영상 파일을 첨부해주세요', upload_to=''),
        ),
    ]
