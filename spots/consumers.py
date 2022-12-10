import json
from channels.generic.websocket import AsyncWebsocketConsumer
import math

all_channels = {}


class ChatConsumer(AsyncWebsocketConsumer):
    PREVIOUS_SPOT = (0, 0)
    CURRENT_SPOT = '0'
    CURRENT_ZOOM = 0

    async def connect(self):
        self.spot_name = self.scope["url_route"]["kwargs"]["spot_name"]
        self.spot_group_name = "spot_%s" % self.spot_name
        self.zoom = self.CURRENT_ZOOM

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

            longitude = text_data_json['spot'][0]
            lon_spot = math.floor(longitude * 10) / 10
            latitude = text_data_json['spot'][1]
            lat_spot = math.floor(latitude * 10) / 10
            # if self.CURRENT_ZOOM >= 18:
            if all_channels.get((lon_spot, lat_spot)):
                all_channels[(lon_spot, lat_spot)].append(
                    {
                        'longlat': (longitude, latitude),
                        'groups': []
                    }
                )
            else:
                all_channels[(lon_spot, lat_spot)] = [{
                    'longlat': (longitude, latitude),
                    'groups': []
                    }]
            print(all_channels)
            # self.spot_group_name = str(lon) + str(lat)
            # await self.channel_layer.group_add(
            #     self.spot_group_name, self.channel_name
            # )
        else:
            message = text_data_json['message']

            await self.channel_layer.group_send(
                self.spot_group_name, {
                    "type": "chat_message", "message": message}
            )

    async def chat_message(self, event):
        message = event["message"]
        print(all_channels)
        await self.send(text_data=json.dumps({"message": message}))
