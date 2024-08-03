from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class ProductCharacteristic(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    characteristic = models.CharField(max_length=255, verbose_name='Характеристика')
    value = models.CharField(max_length=255, verbose_name='Значение')

    def __str__(self):
        return f'{self.product} - {self.characteristic}: {self.value}'

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товара'

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.ManyToManyField(Tag, verbose_name='Теги', related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='product_images/', verbose_name='Картинка')
    is_deleted = models.BooleanField(default=False, verbose_name='Логическое удаление')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Supplier(models.Model):
    company_name = models.CharField(max_length=255, verbose_name='Название компании')
    representative_name = models.CharField(max_length=255, verbose_name='ФИО представителя')
    representative_phone = models.CharField(max_length=255, verbose_name='Телефон представителя')
    address = models.TextField(verbose_name='Адрес')
    is_deleted = models.BooleanField(default=False, verbose_name='Логическое удаление')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class Delivery(models.Model):
    delivery_number = models.CharField(max_length=255, verbose_name='Номер поставки')
    delivery_date = models.DateTimeField(verbose_name='Дата поставки')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик', related_name='deliveries')

    def __str__(self):
        return self.delivery_number

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

class Order(models.Model):
    order_number = models.CharField(max_length=255, verbose_name='Номер заказа')
    customer_name = models.CharField(max_length=255, verbose_name='ФИО покупателя')
    comment = models.TextField(verbose_name='Комментарий')
    delivery_address = models.TextField(verbose_name='Адрес доставки')
    delivery_method = models.CharField(max_length=255, verbose_name='Способ доставки')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    completion_date = models.DateTimeField(verbose_name='Дата завершения')

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Скидка')

    def __str__(self):
        return f'{self.order} - {self.product}'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

class DeliveryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, verbose_name='Поставка')
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')

    def __str__(self):
        return f'{self.delivery} - {self.product}'

    class Meta:
        verbose_name = 'Позиция поставки'
        verbose_name_plural = 'Позиции поставки'

