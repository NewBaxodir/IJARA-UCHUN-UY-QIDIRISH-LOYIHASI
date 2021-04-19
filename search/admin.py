from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Announcement, Photo, Floor, Rooms, Streets
# Register your models here.

admin.site.register(Announcement)
admin.site.register(Photo)
admin.site.register(Streets)

admin.site.register(Floor)
admin.site.register(Rooms)
