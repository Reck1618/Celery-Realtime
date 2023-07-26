from channels.generic.websocket import AsyncWebsocketConsumer
from random import randint
import json
import asyncio

class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Use an asynchronous loop to send 1000 random integers to the client
        for i in range(1000):
            await self.send(json.dumps({'value': randint(-20, 20)}))
            await asyncio.sleep(1)