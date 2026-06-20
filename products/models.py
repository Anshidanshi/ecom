from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete = models.SET_NULL,
        null=True,
        related_name='porducts'
        )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True
    )
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class ProuductColorImage(models.Model):
    prouduct = models.ForeignKey(Product,
                                 on_delete=models.CASCADE,
                                 related_name='color_images'
                                 )
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/colors/')
    
    class Meta:
         unique_together = ('prouduct','color')
        
class ProductVariant(models.Model):
    prouduct = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='variants'
                                )
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=50, unique=True)
    
    class Meta:
         unique_together = ('prouduct','color','size')
    