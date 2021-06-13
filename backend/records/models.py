import datetime

from django.db import models
from django.utils import timezone
import uuid




class Record(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    record_type = models.CharField(max_length=128)
    start_time = models.DateTimeField(blank=False, null=False, default=timezone.now)
    duration = models.FloatField(blank=True, null=True)
    comments = models.TextField(blank=True, default='')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(null=False)

    class Meta:
        ordering = ['start_time']
        indexes = [
            models.Index(fields=['start_time', 'record_type', ]),
        ]

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        print(self.start_time)
        if self.duration:
            self.start_time = timezone.now() - datetime.timedelta(minutes=self.duration)
        print(self.start_time)
        super(Record, self).save(*args, **kwargs)