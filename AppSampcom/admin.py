"""
***********************************
            Packages 
***********************************
"""

# Default
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin


# Model
from AppSampcom.models import (

    # User Model
    User,

    # Hotel Booking
    Hotel,
    Room,
    booking_room



)

"""
*********************************************************************************************************
                                                Custom User Model 
*********************************************************************************************************
"""


# User Admin
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'phone', 'is_active',]

    # list_filter = ['is_active', 'is_staff', ]

    readonly_fields = ["id", "created_on",
                       "updated_on", ]

    fieldsets = (
        ("Register Info:", {"fields": ("id", "email",
         "username", "phone", "password")}),
        ("Personal Info", {
         "fields": ("first_name", "last_name", "full_name"), },),

        ("Login Info", {"fields": ("last_login",), },),
        ("Time Stamp Info", {"fields": ("created_on",
                                        "updated_on"), },),
        ("Permissions", {"fields": ("user_permissions", "groups"), },),
        ("Admin Login", {"fields": ("is_active", "is_superuser",
         "is_staff",), },),
    )


"""
********************
        Hotel 
********************
"""


@admin.register(Hotel)
class Hotel_admin(admin.ModelAdmin):

    list_display = ["id", "hotel_name", "city"]


"""
********************
        Room  
********************
"""


@admin.register(Room)
class Room_admin(admin.ModelAdmin):

    list_display = ["id", "room_type", "room_number", "room_price"]


"""
********************
        Booking  
********************
"""


@admin.register(booking_room)
class Booking_admin(admin.ModelAdmin):

    list_display = ["id", "start_date", "end_date",]
