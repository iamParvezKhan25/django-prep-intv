from django.contrib.auth.models import AbstractUser
from django.db import models


class ApplicationUser(AbstractUser):
    # Using the default fields of AbstractUser (which includes username, first_name, last_name, etc.)
    pass


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_blog_post'

    def __str__(self):
        return self.title
