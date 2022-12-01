"""
*********
Rest Framework
*********
"""

# Permission
from rest_framework import permissions


# Response
from rest_framework.response import Response

# Class - Generic
from rest_framework.generics import GenericAPIView, ListAPIView

# Parser & Status
from rest_framework import status


# Swagger
from drf_yasg.utils import swagger_auto_schema

# Json Web Token
import jwt
from rest_framework_simplejwt.authentication import JWTAuthentication


# Forget Password

# Search & Filter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Q Object
from django.db.models import Q


from django.http import Http404


# Models - Admin
from AppSampcom.models import (

    # User Model
    User,


    # Hotel ,Room, Booking
    Hotel,
    Room,
    booking_room,
)


# Serializers
from AppSampcom.serializers import (

    # Login Serializers
    Login_Serializers,

    # Hotel Serializers
    Hotel_Serializers,
)

"""
**************************************************************************
                            Create Your Business Logic here
**************************************************************************
"""


class Login_Views(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    serializer_class = Login_Serializers

    @ swagger_auto_schema(tags=["Login"], operation_description=("payload", '{"email":"string","password" : "string"}'),)
    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={"request": request})

        if serializer.is_valid(raise_exception=False):

            if User.objects.filter(email=request.data["email"]):
                try:

                    user1 = User.objects.get(email=request.data["email"]).id

                    user = User.objects.get(id=user1)

                    return Response({
                        "response_code": 200,
                        "response_message": _("The Login OTP has been sent to registered phone number. "),
                        "response_data": {
                            "id": user1,
                            "full_name": user.full_name,
                            "token": {'refresh': user.tokens()['refresh'],
                                      'access': user.tokens()['access']}
                        }},
                        status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({"response_code": 400, "response_message": _(e)}, status=status.HTTP_400_BAD_REQUEST)

        else:
            if serializer.errors.get("Invalid_Credentials"):
                return Response({
                    "response_code": 401,
                    "response_message": _("Invalid credentials, try again")},
                    status=status.HTTP_401_UNAUTHORIZED)

        return Response({"response_code": 400, "response_message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


"""
**************************************************************************
                            Hotel List with Room 
**************************************************************************
"""


class Hotel_list_views(GenericAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    serializer_class = Hotel_Serializers

    def get(self, request, format=None):
        data = Hotel.objects.all()
        if data:
            serializer = self.serializer_class(
                data, many=True, context={"request": request})

            return Response(
                {"responseCode": 200,
                 'responseMessage': "Success",
                 'responseData': serializer.data},
                status=status.HTTP_200_OK)


class Search_views(ListAPIView):

    authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [permissions.AllowAny]
    queryset = Hotel.objects.filter(is_active=True)
    serializer_class = Hotel_Serializers
    filter_backends = [SearchFilter]
    search_fields = ["hotel_name", "address", "city", "HotelRoom__room_type"]


class Hotel_Filter_View(ListAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [permissions.AllowAny]
    queryset = Hotel.objects.all()
    serializer_class = Hotel_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bookingHotel__start_date',
                        'bookingHotel__end_date', 'HotelRoom__is_booked', 'HotelRoom__room_type']
