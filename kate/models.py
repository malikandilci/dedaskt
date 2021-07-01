from django.db import models
from django.utils import timezone


class Job(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            blank=True, null=True)

    def create(self):
        self. created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.type
