import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    CURRENT_SPOT = '0'

    async def connect(self):
        self.spot_name = self.scope["url_route"]["kwargs"]["spot_name"]
        self.spot_group_name = "spot_%s" % self.spot_name

        await self.channel_layer.group_add(
            self.spot_group_name, self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.spot_group_name, self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if 'spot' in text_data_json:
            await self.channel_layer.group_discard(
                self.spot_group_name, self.channel_name
            )
            self.spot_name = text_data_json['spot']
            self.spot_group_name = "spot_%s" % self.spot_name

            await self.channel_layer.group_add(
                self.spot_group_name, self.channel_name
            )
        else:
            message = text_data_json['message']
            await self.channel_layer.group_send(
                self.spot_group_name, {
                    "type": "chat_message", "message": message}
            )

    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))
