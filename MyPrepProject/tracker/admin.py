from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TimeRecord


@admin.register(TimeRecord)
class TimeRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'check_in', 'check_out', 'date', 'total_time')
    list_filter = ('date', 'user')
    search_fields = ('user', 'date')
