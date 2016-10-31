from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Problem(models.Model):
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    approval_status = models.BooleanField(default=False)
    solution =  models.TextField(null=True)            

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def _str_(self):
        return self.title