from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from youtube.models import Channel, Video
import json

class BellConsumer(WebsocketConsumer):

    def connect(self):
        if self.scope['user'].is_active:
            self.room_name = self.scope['user']
            self.room_group_name = 'bell_%s' % self.room_name
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()
        else:
            self.room_group_name = 'null'
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.close()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        video_title_json = json.loads(text_data)
        title = video_title_json['title']
        channel = Channel.objects.get(owner=self.scope['user'].id)
        for x in channel.subscribe.all():
            async_to_sync(self.channel_layer.group_send)(
                'bell_%s' % x,
                {
                    'type': 'bell_message',
                    'title': title
                }
            )

    def bell_message(self, event):
        title = event['title']
        self.send(text_data=json.dumps({
            'title': title,
        }))
