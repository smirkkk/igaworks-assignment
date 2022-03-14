from django.db import models

class Event(models.Model):
    event_id = models.CharField(max_length=68)
    user_id = models.CharField(max_length=68)
    event = models.CharField(max_length=50, null=False)
    parameters = models.JSONField()
    event_datetime = models.DateTimeField()
