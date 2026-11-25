from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Product(models.Model):
    '''модель описания продукта'''

    name = models.CharField('название',max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField('описание')
    price = models.DecimalField('цена',max_digits=10, decimal_places=2)
    main_image = models.ImageField('главное изображение',upload_to='products/', blank=True)
    image = models.ImageField('изображение',upload_to='products/', blank=True)
    is_available = models.BooleanField('доступен',default=True)
    created_at = models.DateTimeField('дата создания',auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])

class ProductImage(models.Model):
    """Класс модели для изображений продуктов"""

    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')