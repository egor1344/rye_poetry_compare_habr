from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import GenericViewSet, mixins

from booking.serializers import BookingCreateSerializer


@extend_schema(tags=["Booking"])
class BookingViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = BookingCreateSerializer
