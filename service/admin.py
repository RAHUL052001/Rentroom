from django.contrib import admin

# Register your models here.
from .models import RoomListing, ContactList, User ,AuthUser

admin.site.register(RoomListing)
admin.site.register(ContactList)
admin.site.register(User)
admin.site.register(AuthUser)  # Register the custom user model
