from django.db import models
from django.utils import timezone


class ExpiredCouponManager(models.Manager):
    def expired(self):
        """Return all coupons that are no longer valid."""
        return self.filter(valid_until__lt=timezone.now())


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()

    # attach the custom manager
    objects = ExpiredCouponManager()

    def __str__(self):
        return self.code
