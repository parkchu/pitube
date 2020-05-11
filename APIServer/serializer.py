from rest_framework import serializers
from youtube.models import Channel, Video

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['name', 'channel_photo', 'owner', 'subscribe', 'id']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'video', 'thumbnail', 'owner', 'created', 'good', 'channel', 'id']