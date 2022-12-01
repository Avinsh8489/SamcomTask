"""
**************************
        Packages 
**************************
"""

from django.contrib.auth.models import User, BaseUserManager


"""
********************************************************************************************************
                                            Custom User Model  
********************************************************************************************************
"""


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, phone, password=None, **extra_fields):

        if not username:
            raise ValueError("Username must not be Empty.")

        if not email:
            raise ValueError("Email must not empty.")

        if not phone:
            raise ValueError("Phone must not empty.")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, email, username, phone, password=None, **extra_fields):

        if not password:
            raise ValueError("Password should not be None.")

        user = self.create_user(
            email=email, username=username, phone=phone, password=password)

        user.is_active = True
        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user
