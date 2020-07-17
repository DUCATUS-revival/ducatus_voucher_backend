from django.db import models


class FreezingVoucher(models.Model):
    wallet_id = models.IntegerField(null=True, default=None)
    withdrawn = models.BooleanField(default=False)
    frozen_at = models.DateTimeField(auto_now_add=True)
    redeem_script = models.TextField()
    locked_duc_address = models.CharField(max_length=50)
    user_duc_address = models.CharField(max_length=50)
    user_public_key = models.CharField(max_length=80)