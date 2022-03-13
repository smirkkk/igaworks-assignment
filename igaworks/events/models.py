from django.db import models

class Event(models.Model):
    event_id = models.UUIDField(null=False)
    user_id = models.UUIDField(null=False)
    event = models.CharField(max_length=50, null=False)
    parameters = models.JSONField()
    event_datetime = models.DateTimeField()
