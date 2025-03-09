from django.contrib.admin import ModelAdmin, register

from ..models import Hotel


@register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display = ('id', 'name')

