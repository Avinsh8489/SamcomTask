"""
*************************************
        Imported Packages 
*************************************
"""

# Serializer
from dataclasses import field
from email.policy import default
from rest_framework import serializers

# DateTime
from datetime import datetime

# Translation
from django.utils.translation import gettext_lazy as _

# Setting.py
from django.conf import settings

# Regular Expression
import re

# Authutication
from django.contrib import auth
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# Default Util - Forget Password
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

# JSON
import json

# Q Object
from django.db.models import Q


# Admin Models
from AppSampcom.models import (

    # Custom User
    User,


    # Hotel ,Room, Booking
    Hotel,
    Room,
    booking_room,

)


"""
****************************************************************************************************************************************************************
                                                                 Admin
****************************************************************************************************************************************************************
"""


"""
********************
    Register Admin
********************
"""


class Login_Serializers(serializers.Serializer):

    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=50)
    # class Meta:
    #     model = User
    #     fields = ["id", "email", "password"]

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            # email = User.objects.get(email=email)

            # print(f"\n\n\n\n {email} \n\n\n")

            user = auth.authenticate(email=email, password=password)

            # Raise AuthenticationFailed
            if not user:
                raise serializers.ValidationError(
                    {"Invalid_Credentials": _('Invalid credentials, try again')})

        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"Invalid_Credentials": _('Invalid credentials, try again')})
        return attrs


"""
****************************************************************************************************************************************************************
                                                                 Hotel List 
****************************************************************************************************************************************************************
"""


"""
********************
    Room  
********************
"""


# class Hotel_Serializers(serializers.ModelSerializer):

#     # hotel_room_id = Room_Serializers(many=True)

#     class Meta:
#         model = Hotel
#         fields = ["id", "hotel_name", "address",
#                   "city", "gst_no", ]


class Room_Serializers(serializers.ModelSerializer):

    # hotel_room_id = Hotel_Serializers(many=True)

    class Meta:
        model = Room
        fields = ["id", "hotel_room_id", "room_type",
                  "room_number", "room_price", "is_booked"]


class Hotel_Serializers(serializers.ModelSerializer):

    HotelRooms = Room_Serializers(many=True)

    class Meta:
        model = Hotel
        fields = ["id", "hotel_name", "address",
                  "city", "gst_no", "HotelRooms"]


# class Hotel_Serializers(serializers.ModelSerializer):

#     HotelRooms = Room_Serializers(many=True)

#     class Meta:
#         model = Hotel
#         fields = ["id", "hotel_name", "address",
#                   "city", "gst_no", "HotelRooms"]
