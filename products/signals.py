from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from . models import Product, Category,ProductColorImage

@receiver(pre_save, sender=Product)
def generate_product_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        
@receiver(pre_save, sender=Category)
def generate_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        
@receiver(post_delete, sender=ProductColorImage)
def delete_color_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)