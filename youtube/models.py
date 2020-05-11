from django.db import models
from account.models import User

class Channel(models.Model):
    name = models.CharField(max_length=100)
    channel_photo = models.ImageField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    subscribe = models.ManyToManyField(User, related_name='subscribe')

    @property
    def total_subscribe(self):
        return self.subscribe.count()

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(null=False, help_text="동영상 파일을 첨부해주세요")
    thumbnail = models.ImageField(null=True, help_text="썸네일 사진을 첨부해주세요")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_user', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    good = models.ManyToManyField(User, related_name='like', default=None)
    channel = models.ForeignKey(Channel, related_name='channel_name', on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return self.title

    @property
    def total_good(self):
        return self.good.count()
