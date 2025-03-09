import uuid

from django.db import models

from hotel.models import HotelSuite
from .customer import Customer


class Booking(models.Model):
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    suite = models.ForeignKey(HotelSuite, verbose_name='Номер отеля', on_delete=models.CASCADE)
    from_date = models.DateField('С какой даты')
    to_date = models.DateField('До какой даты')

    customers = models.ManyToManyField(Customer, verbose_name='Посетители')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f"Бронирование отеля с {self.from_date} до {self.to_date}"
