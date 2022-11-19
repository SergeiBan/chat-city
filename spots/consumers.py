from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    PatchModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DeleteModelMixin
)
from djangochannelsrestframework.decorators import action
from spots.models import Spot
from spots.serializers import SpotSerializer


class SpotConsumer(
    ListModelMixin,
    RetrieveModelMixin,
    PatchModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
    GenericAsyncAPIConsumer
):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

    @action()
    def say(self, pk=None, **kwargs):
        spot = self.get_object(pk=pk)
        return {'answer': 'well well well'}, 200