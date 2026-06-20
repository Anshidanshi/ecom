from django.db import models


class Category(models.Model):
    name       = models.CharField(max_length=100, unique=True)
    slug       = models.SlugField(max_length=100, unique=True)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name         = models.CharField(max_length=100)
    slug         = models.SlugField(max_length=100, unique=True)
    category     = models.ForeignKey(
                       Category,
                       on_delete=models.SET_NULL,
                       null=True,
                       related_name='products'
                   )
    description  = models.TextField()
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    old_price    = models.DecimalField(
                       max_digits=10, decimal_places=2,
                       null=True, blank=True
                   )
    is_available = models.BooleanField(default=True)
    is_featured  = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['is_available', 'is_featured']),
        ]

    def __str__(self):
        return self.name


class ProductColorImage(models.Model):
    product = models.ForeignKey(
                  Product,
                  on_delete=models.CASCADE,
                  related_name='color_images'
              )
    color   = models.CharField(max_length=50)
    image   = models.ImageField(upload_to='products/colors/')

    class Meta:
        unique_together = ('product', 'color')

    def __str__(self):
        return f"{self.product.name} - {self.color}"


class ProductVariant(models.Model):
    product = models.ForeignKey(
                  Product,
                  on_delete=models.CASCADE,
                  related_name='variants'
              )
    color   = models.CharField(max_length=50)
    size    = models.CharField(max_length=50)
    stock   = models.PositiveIntegerField(default=0)
    sku     = models.CharField(max_length=50, unique=True)

    class Meta:
        unique_together = ('product', 'color', 'size')

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"