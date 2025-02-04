from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from prep_app.models import ApplicationUser


class TimeRecord(models.Model):
    user = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)  # Replace with ForeignKey if using Django's User model
    check_in = models.DateTimeField(default=timezone.now)
    check_out = models.DateTimeField(null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.date}"

    def total_time(self):
        if self.check_out:
            duration = self.check_out - self.check_in
            total_seconds = int(duration.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        return "00:00:00"

    def save(self, *args, **kwargs):
        self.date = timezone.now().date()  # Ensure the date is always set to today
        super().save(*args, **kwargs)
