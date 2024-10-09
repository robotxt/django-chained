from django.db import models

class BaseDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class EventData(BaseDate):
    nft_address = models.CharField(max_length=300)
    token_id = models.IntegerField()
    block_number = models.IntegerField()
    from_address = models.CharField(max_length=300)
    to_address = models.CharField(max_length=300)
    transaction_hash = models.CharField(max_length=300)

    class Meta:
        unique_together = ("token_id", "block_number")
