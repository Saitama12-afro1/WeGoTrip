from django.db import models


class Product(models.Model):
    """Описывает товары"""
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='product_pictures/%Y/%m/%d')
    content = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "product"
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self) -> str:
        return f"{self.name} + {self.price}"



class Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.status}'


class Order(models.Model):
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    date_create = models.DateTimeField(auto_now_add=True)
    date_confirmation = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(to = 'Status', blank=True, null=True, on_delete=models.CASCADE, related_name='orders')


    class Meta:
        db_table = "order"
        verbose_name = 'order'
        verbose_name_plural = 'orders'
    

    def __str__(self) -> str:
        return f'{self.total_sum}'

class TypePayment(models.Model):
    type_payment = models.CharField(max_length=100)
    

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(to = 'Status', blank=True, null=True, on_delete=models.CASCADE, related_name='payments')
    type_payment = models.ForeignKey(to = 'TypePayment', blank=True, null=True, on_delete=models.CASCADE, related_name='payments')
    order = models.OneToOneField(to = "Order", blank=True, null=True, default=None,
                                  on_delete=models.CASCADE, related_name='payments',
                                  )

    class Meta:
        db_table = "payment"
        verbose_name = 'payment'
        verbose_name_plural = 'payments'











    
