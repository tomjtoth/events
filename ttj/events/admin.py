from django.contrib import admin

# Register your models here.

from .models import Event, Activity

admin.site.register(Event)
admin.site.register(Activity)
