from django.db import models
from django.utils import timezone
from authentication.models import User

class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=False, blank=False)
    catergory = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateField(timezone.now())
    updated_at = models.DateField(timezone.now())


    def __str__(self):
        return f"{self.owner}-{self.created_at}"
