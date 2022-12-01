"""
***********************************
            Packages 
***********************************
"""

# Default
from django.db import models

# Custom User Model Manager
from AppSampcom.UserManager import CustomUserManager

# AbstractUser
from django.contrib.auth.models import AbstractUser


# JWT
from rest_framework_simplejwt.tokens import RefreshToken


"""
*********************************************************************************************************
                                                Custom User Model 
*********************************************************************************************************
"""


class User(AbstractUser):

    full_name = models.CharField(max_length=256, null=True, blank=True)

    email = models.EmailField(max_length=254, unique=True)

    phone = models.CharField(max_length=50, unique=True)

    username = models.CharField(
        max_length=50, null=True, blank=True, unique=True)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    is_active:  models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "username"]

    object = CustomUserManager()

    def __str__(self):
        return self.first_name

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}


"""
*********************
    Hotel Model 
*********************
"""


class Hotel(models.Model):

    hotel_name = models.CharField(max_length=100)
    address = models.TextField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=50)

    gst_no = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hotel_name


class Room(models.Model):

    hotel_room_id = models.ForeignKey(Hotel,  on_delete=models.CASCADE,
                                      related_name="HotelRooms",
                                      related_query_name="HotelRoom",
                                      limit_choices_to={"is_active": True})

    room_type = models.CharField(max_length=50, choices=(
        ("Single Bed", "Single Bed"),
        ("Double Bed",
         "Double Bed"),
        ("Luxury Room", "Luxury Room")), default="Single Bed")

    room_number = models.IntegerField()
    room_price = models.IntegerField()

    is_booked = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hotel_room_id} - {self.room_type}"


class booking_room(models.Model):

    user_id = models.ForeignKey(User,  on_delete=models.CASCADE,
                                related_name="UserBooking",
                                related_query_name="UserBookings",
                                limit_choices_to={"is_active": True})

    hotel_booking_id = models.ForeignKey(Hotel,  on_delete=models.CASCADE,
                                         related_name="bookingHotels",
                                         related_query_name="bookingHotel",
                                         limit_choices_to={"is_active": True})

    room_id = models.ForeignKey(Room,  on_delete=models.CASCADE,
                                related_name="RoomNumbers",
                                related_query_name="RoomNumber",
                                limit_choices_to={"is_active": True})

    start_date = models.DateField()
    end_date = models.DateField()

    is_active = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        start = str(self.start_date)
        end = str(self.end_date)
        return f"{start} - {end}"
