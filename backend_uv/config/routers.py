from rest_framework.routers import SimpleRouter

from booking.viewset import BookingViewSet
from hotel.viewset import HotelViewSet
from users.viewsets import UserViewSet

router = SimpleRouter()

router.register(r"users", UserViewSet, "users")
router.register(r"hotel", HotelViewSet, "hotel")
router.register(r"booking", BookingViewSet, "booking")
