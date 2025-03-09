from rest_framework import serializers

from booking.models import Booking


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Booking
