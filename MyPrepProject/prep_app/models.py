from django.contrib.auth.models import AbstractUser


class ApplicationUser(AbstractUser):
    # Using the default fields of AbstractUser (which includes username, first_name, last_name, etc.)
    pass
