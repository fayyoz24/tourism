from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.appvars import APP_NAME
import os
from .functions import user_dir, user_default_pro_pic, file_size
# import question.models
# Create your models here.

class User(AbstractUser):
    username=models.CharField(max_length=100, unique=True)
    # email=models.EmailField(max_length=100, unique=True)
    first_name=models.CharField(max_length=100, blank=True, null=True)
    last_name=models.CharField(max_length=100, blank=True, null=True)
    USER_TYPE_CHOICES = [('U', 'COMMON_USER'), ('G', 'GUIDE'),
                      ('A', 'ADMIN'), ('C', 'TOUR_COMPANY')]

    pro_pic = models.ImageField(default=user_default_pro_pic,
                            upload_to=user_dir,
                            verbose_name="Profile Picture",
                            validators=[file_size])

    # Default user_type must be defined to enforce security
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, verbose_name="User Type", default='U')
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def __str__(self):
        return self.username


class BlockedIP(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # To know which user blocked this IP
    ip_address = models.GenericIPAddressField(unique=True)  # Store IP addresses
    created_at = models.DateTimeField(auto_now_add=True)  # Track when it was added

    def __str__(self):
        return f"{self.user_name if self.user_name else 'Unknown'} -- {self.ip_address}"