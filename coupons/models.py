from django.db import models
from django.utils import timezone
# Create your models here.

class Coupon(models.Model):
    class Type(models.TextChoices):
        PERCENTAGE = 'percentage', 'Percentage'
        FIXED = 'fixed', 'Fixed'
    code = models.CharField(max_length=50, unique=True)
    discount_type = models.CharField(
                        max_length=50, 
                        choices=Type.choices, 
                        default=Type.PERCENTAGE
                        )
    discount_value = models.DecimalField(max_digits=6, decimal_places=2)
    min_order_value = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    max_uses = models.PositiveIntegerField(default=10)
    used_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
        
    def is_valid(self):
        expired = self.expiry_date < timezone.now()
        return (self.is_active and not expired and self.used_count < self.max_uses)