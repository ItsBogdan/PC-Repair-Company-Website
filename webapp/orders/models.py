from django.db import models
from django.contrib.auth.models import User

#Создание класса списка услуг
class Device(models.Model):
    device = models.CharField(max_length=50)

    def __str__(self):
        return self.device
class ListOfServices(models.Model):
    service_name = models.CharField(verbose_name='Услуга', max_length=50)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='Устройство')

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Client(models.Model):
    client_id = models.BigAutoField(primary_key=True, verbose_name='ID клиента')
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.CharField(max_length=30, verbose_name='Адрес эл.почты')
    username = models.CharField(max_length=30, verbose_name='Имя пользователя')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

#Создание класса заказа
class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True, verbose_name='Номер заказа')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    service = models.ForeignKey(ListOfServices, on_delete=models.CASCADE, verbose_name='Услуга')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='Устройство')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата обращения')
    STATUS = (
        ('W', 'В ожидании'),
        ('P', 'В работе'),
        ('D', 'Выполнено'),
    )
    status = models.CharField(max_length=1, choices=STATUS, default='W', verbose_name='Статус')
    price = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Цена', blank=True, null=True)

    def __str__(self):
        return str(self.order_id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'