from django.db import models
from django.conf import settings


class Review(models.Model):
    class Rating(models.IntegerChoices):
        ONE   = 1, '1 Star'
        TWO   = 2, '2 Stars'
        THREE = 3, '3 Stars'
        FOUR  = 4, '4 Stars'
        FIVE  = 5, '5 Stars'

    user    = models.ForeignKey(
                  settings.AUTH_USER_MODEL,
                  on_delete=models.CASCADE,
                  related_name='reviews_written'
              )
    product = models.ForeignKey(
                  'products.Product',
                  on_delete=models.CASCADE,
                  related_name='reviews'
              )
    rating    = models.IntegerField(choices=Rating.choices)
    comment   = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        ordering        = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - {self.product.name} ({self.rating}★)"