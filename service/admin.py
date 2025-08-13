from django.contrib import admin

# Register your models here.
from .models import RoomListing, ContactList, User ,authuser

admin.site.register(RoomListing)
admin.site.register(ContactList)
admin.site.register(User)
admin.site.register(authuser)  # Register the custom user model
