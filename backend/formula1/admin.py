from django.contrib import admin
from .models import Formula1, Drivers, Races, Teams

admin.site.register(Formula1)
admin.site.register(Drivers)
admin.site.register(Races)
admin.site.register(Teams)