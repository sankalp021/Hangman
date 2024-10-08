from django.db import models
import uuid
class Word(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # This will store the string

    def __str__(self):
        return self.name
