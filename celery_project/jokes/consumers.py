from channels.generic.websocket import AsyncWebsocketConsumer
import json

class JokeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'jokes_group'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected to the server.'
        }))
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_joke(self, event):
        joke = event['text']

        await self.send(text_data=json.dumps({
            'type': 'send_joke',
            'text': joke
        }))