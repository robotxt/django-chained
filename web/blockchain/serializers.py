from rest_framework import serializers
from blockchain.models import EventData


class EventDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventData
        fields = "__all__"
