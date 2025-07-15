from django.contrib import admin

# Register your models here.
from .models import RoomListing, ContactList, User

admin.site.register(RoomListing)
admin.site.register(ContactList)
admin.site.register(User)
