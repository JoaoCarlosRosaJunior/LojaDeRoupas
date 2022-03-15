# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from django.core import serializers
from asyncio import sleep
from lojaapp.models import Produto
from asgiref.sync import sync_to_async
class CartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # # Join room group
        # await self.channel_layer.group_add(
        #     self.cart_name,
        #     self.channel_name
        # )

        while True:
            query = await database_sync_to_async(Produto.objects.all)()
            json_resp = await sync_to_async(serializers.serialize)("json",query)
            await self.send(json_resp)
            #await sleep(0.01)

        

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

