from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class StatusChoices(models.TextChoices):
    paid = ('paid', "Paid")
    not_paid = ('not_paid', "Not Paid")
    expired = ('expired', "Expired")


class Advertisement(models.Model):
    seller = models.ForeignKey(User, related_name='seller', on_delete=models.CASCADE)
    title = models.CharField(max_length=66, blank=True)
    description = models.TextField(blank=True)
    video = models.FileField()
    price = models.PositiveIntegerField(blank=True, null=True)
    duration = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices=StatusChoices.choices)
    is_validated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.price = int(self.duration * 100)
        super(Advertisement, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.video.url}'