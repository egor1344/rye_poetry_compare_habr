import uuid

from django.db import models

from hotel.constant import HotelSuiteType
from hotel.models.hotel import Hotel


class HotelSuite(models.Model):
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)

    hotel = models.ForeignKey(Hotel, verbose_name='Отель', on_delete=models.CASCADE)
    number = models.IntegerField('Номер')
    type = models.IntegerField('Тип', choices=HotelSuiteType.choices, default=HotelSuiteType.STD)
    floor = models.IntegerField('Этаж')
    rooms = models.IntegerField('Количество комнат')

    class Meta:
        verbose_name = 'Номер в отеле'
        verbose_name_plural = 'Номера в отеле'

    def __str__(self):
        return f"Номер отеля {self.number}"
