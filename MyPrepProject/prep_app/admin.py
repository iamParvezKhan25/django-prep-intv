from django.contrib import admin

# Register your models here.
from .models import ApplicationUser, BlogPost

admin.site.register(ApplicationUser)
admin.site.register(BlogPost)
