from django.db import models
from django.contrib.postgres.fields import ArrayField


class Type(models.Model):
    text = models.JSONField()
    type = models.CharField(max_length=50)
    keys = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)
    
    class Meta:
        db_table = 'sms_types'

    def __str__(self) -> str:
        return f"SmsType(pk={self.pk})"