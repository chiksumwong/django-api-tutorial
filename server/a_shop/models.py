import uuid

from django.db import models

from server import settings


class Mayor(models.Model):
    mayor_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    mayor_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'a_mayor'

    def __str__(self):
        return self.mayor_name


class City(models.Model):
    city_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    city_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    mayor = models.OneToOneField(Mayor, on_delete=models.CASCADE)  # One to One

    class Meta:
        db_table = 'a_city'

    def __str__(self):
        return self.city_name


class Customer(models.Model):
    customer_status = {
        (0, 'inactive'),
        (1, 'active')
    }
    customer_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=100)
    customer_status = models.SmallIntegerField(choices=customer_status, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)  # FK of 'City', if is other app 'app.City'
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # One to One

    class Meta:
        db_table = 'a_customer'

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    product_image = models.ImageField(upload_to='product_image')
    created_at = models.DateTimeField(auto_now_add=True)
    customers = models.ManyToManyField(Customer, through='Order', through_fields=('product', 'customer'))
    # Many to Many through "Order"

    class Meta:
        db_table = 'a_product'

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # FK of 'Customer'
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # FK of 'Product'

    class Meta:
        db_table = 'a_order'

    def __str__(self):
        return self.order_id


class OrderAttachment(models.Model):
    order_attachment_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='order')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order_attachment"

    def __str__(self):
        return self.order
