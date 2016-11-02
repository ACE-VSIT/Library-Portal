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
    attendance_status =   models.BooleanField(default=False)                                   

    def _str_(self):
        return self.attendance_status        


class EventNameDate(models.Model):            
    event_name = models.CharField(max_length=200)
				date_id	=	models.integerfield(default=0)
				created_date = models.DateTimeField(
            default=timezone.now)

    def record(self):
        self.created_date = timezone.now()
        self.save()

class Resource(models.Model):
    author = models.ForeignKey('auth.User')                
    resource_category = models.CharField(max_length=200)
    resource_title = models.CharField(max_length=200)
				resource_desc = models.CharField(max_length=20000)    
    resource_approval =   models.BooleanField(default=False)
				resource_id	=	models.integerfield(default=0)						                                   

    def _str_(self):
        return self.resource_approval        
        