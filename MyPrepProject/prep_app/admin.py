from django.contrib import admin

# Register your models here.
from .models import ApplicationUser

admin.site.register(ApplicationUser)
