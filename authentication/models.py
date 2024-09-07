from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    hashed_refresh_token = models.CharField(max_length=255)
    last_ip_address = models.GenericIPAddressField()
