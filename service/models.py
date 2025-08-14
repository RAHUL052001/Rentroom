from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class AuthUserManager(BaseUserManager):
    print("33333333333333333333333333333333333333333")
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class AuthUser(AbstractBaseUser, PermissionsMixin):
    print("uuuuuuuuuuuuuuuuuu")
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AuthUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)

class User(models.Model):
    """
    User model for MongoDB using mongoengine.
    """
    username = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(unique=True,null=False, blank=False)      
    Is_owner = models.BooleanField(default=False,null=False, blank=False)  # True if the user is a room owner
    first_name = models.CharField(max_length=100,null=False, blank=False)
    last_name = models.CharField(max_length=100,null=False, blank=False)
    password = models.CharField(max_length=100,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True,null=False, blank=False)

    def __str__(self):
        return str(self.email)
    

class RoomListing(models.Model):
    """
    Room listing model for MongoDB using mongoengine.
    """
    room_type = models.CharField(max_length=100,null=False, blank=False)  # e.g., 'Single', 'Double', etc.
    room_name = models.CharField(max_length=200, null=False, blank=False)
    room_capacity = models.IntegerField(null=False, blank=False)  # Number of people the room can accommodate
    rom_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)  # Owner of the room
    room_description = models.TextField(null=False, blank=False)  # Detailed description of the room
    room_image = models.CharField(max_length=255, null=False, blank=False)  # URL or path to the room image
    room_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)  # Price per night
    room_location =models.CharField(max_length=255, null=False, blank=False)  # Location of the room
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)  # Timestamp when the room was listed

    def __str__(self):
        return  str(self.room_name)
    
class ContactList(models.Model):
    """
    Contact list model for MongoDB using mongoengine.
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    RoomListing = models.ForeignKey(RoomListing, on_delete=models.CASCADE, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)  # Timestamp when the contact was made

    def __str__(self):
        return str(self.name)


   
