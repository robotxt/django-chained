from rest_framework import serializers
from blockchain.models import EventData


class EventDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventData
        fields = [
            "id",
            "token_id",
            "block_number",
            "from_address",
            "to_address",
            "transaction_hash",
        ]
