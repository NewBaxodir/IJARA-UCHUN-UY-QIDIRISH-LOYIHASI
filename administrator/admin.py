from django.contrib import admin

# Register your models here.
from .models import User, Useradminpage, Householder
# Register your models here.

admin.site.register(User)
admin.site.register(Useradminpage)
admin.site.register(Householder)

