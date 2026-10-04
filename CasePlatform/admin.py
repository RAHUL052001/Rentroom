import django
from django.contrib import admin

from CasePlatform.models import INP_CASE, INP_CASE_META, INP_MILESTONE

# Register your models here.

admin.site.register(INP_CASE)
admin.site.register(INP_CASE_META)
admin.site.register(INP_MILESTONE)
    
