from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from blockchain.serializers import EventDataSerializer
from blockchain.models import EventData


class BaseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    pass


class EventDataApiEndpoint(BaseViewSet):
    serializer_class = EventDataSerializer
    queryset = EventData.objects.filter(deleted_at=None)

    def list(self, request):
        events = self.get_queryset()
        page = self.paginate_queryset(events.order_by("-created_at"))

        serialize = self.get_serializer(page, many=True)
        return self.get_paginated_response(serialize.data)

    def retrieve(self, request, *args, **kwargs):
        token_id = kwargs["pk"]
        event = self.get_queryset().get(token_id=token_id)
        serialize = self.get_serializer(event)
        return Response(serialize.data)
