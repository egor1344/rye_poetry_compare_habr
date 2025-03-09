from django.contrib.admin import ModelAdmin, register, RelatedOnlyFieldListFilter

from ..models import Booking


@register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = ('id', 'suite', 'from_date', 'to_date')
    list_filter = [
        ("suite", RelatedOnlyFieldListFilter),
        'from_date', 'to_date'
    ]
