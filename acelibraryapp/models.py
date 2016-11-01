from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Problem(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    approval_status =   models.BooleanField(default=False)
    solution    =   models.TextField(
            blank=True, null=True
    )            

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def _str_(self):
        return self.title

class Attendance(models.Model):
    person_name = models.CharField(max_length=200)        
    created_date = models.DateTimeField(
            default=timezone.now)
    agenda = models.CharField(max_length=200)
    event_name = models.CharField(max_length=200)
    attendance_status =   models.BooleanField(default=False)                                   

    def record(self):
        self.created_date = timezone.now()
        self.save()

    def _str_(self):
        return self.attendance_status        