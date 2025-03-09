from django.contrib.admin import ModelAdmin, register

from ..models import Customer


@register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'phone', 'email')
