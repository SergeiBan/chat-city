import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    CURRENT_SPOT = '0'

    def connect(self):
        self.spot_name = self.scope["url_route"]["kwargs"]["spot_name"]
        self.spot_group_name = "spot_%s" % self.spot_name

        async_to_sync(self.channel_layer.group_add)(
            self.spot_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.spot_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if 'spot' in text_data_json:
            async_to_sync(self.channel_layer.group_discard)(
                self.spot_group_name, self.channel_name
            )
            self.spot_name = text_data_json['spot']
            self.spot_group_name = "spot_%s" % self.spot_name

            async_to_sync(self.channel_layer.group_add)(
                self.spot_group_name, self.channel_name
            )
        else:
            message = text_data_json['message']
            async_to_sync(self.channel_layer.group_send)(
                self.spot_group_name, {"type": "chat_message", "message": message}
            )

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"message": message}))
