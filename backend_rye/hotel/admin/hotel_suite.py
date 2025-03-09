from django.contrib.admin import ModelAdmin, register

from ..models import HotelSuite


@register(HotelSuite)
class HotelSuiteAdmin(ModelAdmin):
    list_display = ('id', 'hotel', 'number', 'type', 'floor', 'rooms')
