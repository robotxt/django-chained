import json
from django.conf import settings
from django.core.management.base import BaseCommand

from web3 import Web3
from blockchain.models import EventData


class Command(BaseCommand):
    help = "Retrieve Contract Events"

    def handle(self, *args, **options):
        with open('blockchain/abi.json', 'r') as abi_definition:
            abi = json.load(abi_definition)

        w3 = Web3(Web3.HTTPProvider(settings.INFURA_MAINNET_HTTP))
        address = w3.to_checksum_address(settings.BAYC_ADDRESS)
        contract = w3.eth.contract(address, abi=abi)

        # This will return 10000 records
        event_filter = contract.events.Transfer.create_filter(from_block="0xBB933A", to_block="0xBC676B")

        items = event_filter.get_all_entries()[-10:]  # store the last 10 results
        transfer_events = []
        for item in items:
            data = json.loads(Web3.to_json(item))
            event_args = data["args"]

            transfer_events.append(EventData(
                nft_address=address,
                token_id=event_args["tokenId"],
                block_number=data["blockNumber"],
                from_address=event_args["from"],
                to_address=event_args["to"],
                transaction_hash=data["transactionHash"]
            ))

        EventData.objects.bulk_create(transfer_events)
