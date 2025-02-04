from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TimeRecord
import pytz
from datetime import timedelta


# Check-in View
def check_in(request):
    if request.method == 'POST':
        user = request.user
        kolkata_tz = pytz.timezone('Asia/Kolkata')
        current_time = timezone.now().astimezone(kolkata_tz)
        open_record = TimeRecord.objects.filter(user=user, date=current_time.date(), check_out__isnull=True).first()
        if not open_record:
            TimeRecord.objects.create(user=user, check_in=current_time)
        return redirect('dashboard')


# Check-out View
def check_out(request):
    if request.method == 'POST':
        user = request.user
        kolkata_tz = pytz.timezone('Asia/Kolkata')
        current_time = timezone.now().astimezone(kolkata_tz)
        open_record = TimeRecord.objects.filter(user=user, date=current_time.date(), check_out__isnull=True).first()
        if open_record:
            open_record.check_out = current_time
            open_record.save()
        return redirect('dashboard')


# Dashboard View
def dashboard(request):
    user = request.user
    kolkata_tz = pytz.timezone('Asia/Kolkata')
    records = TimeRecord.objects.filter(user=user, date=timezone.now().date())

    for record in records:
        record.check_in = record.check_in.astimezone(kolkata_tz)
        if record.check_out:
            record.check_out = record.check_out.astimezone(kolkata_tz)

    # Calculate total time worked in seconds
    total_seconds = sum(
        (record.check_out - record.check_in).total_seconds()
        for record in records
        if record.check_out
    )

    # Convert total seconds to HH:MM:SS format
    total_time = str(timedelta(seconds=int(total_seconds)))

    context = {
        'records': records,
        'total_time': total_time,
    }
    return render(request, 'dashboards.html', context)
