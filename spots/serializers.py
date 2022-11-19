from rest_framework import serializers
from spots.models import Spot


class MessageSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=128)
    user_id = serializers.SerializerMethodField()
    spot = serializers.IntegerField()

    class Meta:
        fields = ('text', 'user_id', 'spot')

    def get_user_id(self):
        return self.context['request'].user.pk


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('x', 'y')
