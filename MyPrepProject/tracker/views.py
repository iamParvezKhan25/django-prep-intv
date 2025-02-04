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

    # Fetch records for the current day and order by check_in time in descending order
    records = TimeRecord.objects.filter(user=user, date=timezone.now().date()).order_by('-check_in')

    # Convert UTC times to Asia/Kolkata timezone
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

    # Calculate remaining time (8 hours 30 minutes = 30600 seconds)
    work_limit_seconds = 8 * 3600 + 30 * 60  # 8 hours 30 minutes in seconds
    remaining_seconds = max(0, work_limit_seconds - total_seconds)
    total_remain_time = str(timedelta(seconds=int(remaining_seconds)))

    context = {
        'records': records,
        'total_time': total_time,
        'total_remain_time': total_remain_time,  # Add remaining time to context
    }
    return render(request, 'dashboards.html', context)

