from django.db import models
from Users.models import User

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, primary_key=False, unique=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'категории'

class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'Продукт: {self.name} | Kатегория: {self.category}'


class BasketQuerySet(models.QuerySet):

    def total_sum(self):
        return sum([basket.sum() for basket in self])

    def total_quantity(self):
        return sum([basket.quantity for basket in self])

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

