from django.contrib import admin
from youtube.models import Video, Channel

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
