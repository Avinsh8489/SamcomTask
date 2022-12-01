"""
******************************
        Packages 
******************************
"""

# Default Packages
from django.contrib import admin
from django.urls import path, include


from AppSampcom.views import (

    # User Login Api
    Login_Views,


    # Hotel List Views
    Hotel_list_views,

    # Search_views
    Search_views,

    # Filter
    Hotel_Filter_View
)
"""
************************************************************************************************************************
                                        URLS
************************************************************************************************************************
"""
urlpatterns = [

    # User Login API
    path("User-Login", Login_Views.as_view(), name="UserLoginAPI"),

    # Hotel List Views
    path("Hotel-List/", Hotel_list_views.as_view(), name="HotelListViews"),

    # Search View
    path("Search/", Search_views.as_view(), name="SearchHotel"),


    # Filter

    path("Filter/", Hotel_Filter_View.as_view(), name="FilterHotel")

]
