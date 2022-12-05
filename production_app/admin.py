from django.contrib import admin

from django.contrib import admin

from .models import Garden, Crop, Variety, Harvest, Timeline

admin.site.register(Garden)
admin.site.register(Crop)
admin.site.register(Variety)
admin.site.register(Harvest)
admin.site.register(Timeline)
