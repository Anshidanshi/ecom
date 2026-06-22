from django.db import models
from django.conf import settings


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING    = 'pending',    'Pending'
        PROCESSING = 'processing', 'Processing'
        SHIPPED    = 'shipped',    'Shipped'
        DELIVERED  = 'delivered',  'Delivered'
        CANCELLED  = 'cancelled',  'Cancelled'

    class PaymentStatus(models.TextChoices):
        UNPAID   = 'unpaid',   'Unpaid'
        PAID     = 'paid',     'Paid'
        REFUNDED = 'refunded', 'Refunded'

    user           = models.ForeignKey(
                         settings.AUTH_USER_MODEL,
                         on_delete=models.PROTECT,
                         related_name='orders'
                     )
    coupon         = models.ForeignKey(
                         'coupons.Coupon',
                         on_delete=models.SET_NULL,
                         null=True, blank=True,
                         related_name='orders'
                     )
    full_name      = models.CharField(max_length=200)
    email          = models.EmailField()
    phone          = models.CharField(max_length=20)
    address        = models.TextField()
    city           = models.CharField(max_length=100)
    state          = models.CharField(max_length=100)
    pincode        = models.CharField(max_length=20)
    total_price    = models.DecimalField(max_digits=10, decimal_places=2)
    status         = models.CharField(
                         max_length=20,
                         choices=Status.choices,
                         default=Status.PENDING
                     )
    payment_status = models.CharField(
                         max_length=20,
                         choices=PaymentStatus.choices,
                         default=PaymentStatus.UNPAID
                     )
    payment_id     = models.CharField(max_length=200, blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} — {self.full_name}"


class OrderItem(models.Model):
    order    = models.ForeignKey(
                   Order,
                   on_delete=models.CASCADE,
                   related_name='items'
               )
    variant  = models.ForeignKey(
                   'products.ProductVariant',
                   on_delete=models.PROTECT,
                   related_name='order_items'
               )
    quantity = models.PositiveIntegerField(default=1)
    price    = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} × {self.variant.product.name} ({self.variant.color}/{self.variant.size})"

    @property
    def total_price(self):
        return self.price * self.quantity