from datetime import timedelta

from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=66, blank=True)
    description = models.TextField(blank=True)
    video = models.FileField()
    price = models.PositiveIntegerField(blank=True, null=True)
    duration = models.PositiveIntegerField()
    is_validated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.price = int(self.duration * 100)
        super(Advertisement, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.video.url}'