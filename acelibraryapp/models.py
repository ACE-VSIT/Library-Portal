from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):

    #name,enrollNumebr,email_id
    name = models.CharField(max_length=50)
    enroll_number = models.PositiveIntegerField(primary_key=True)
    email_id = models.EmailField(max_length=50,unique=True)

    def __unicode__(self):
        return self.name

    class Meta :
        ordering = ['name']



class User(models.Model):

    #enroll_number(foreign key), date of joining, ifACE, ifCore, domain , contact

    enroll_number = models.ForeignKey(Student)
    join_date = models.DateTimeField(null=True)
    ifACE = models.BooleanField()
    ifCore = models.BooleanField()
    domain_choices= (('a','Programming'),('b','Web Development'),('c','Graphic Desgning'),('d','A/V Editing'),('e','Other'))

    domain = models.CharField(max_length=1,choices = domain_choices)



class Tasks(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    approval_status = models.BooleanField(default=False)
    solution =  models.TextField(blank=True,null=True)            

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def _str_(self):
        return self.title


class Events(models.Model):


    ID = models.TextField(primary_key = True)
    date = models.DateTimeField(default=timezone.now)
    name = models.TextField(max_length=30)
    description = models.TextField(blank=True,null=True)

    def __init(self):
        self.date=timezone.now()
        self.save()

    def _str_(self):
        return self.name



'''
class Resources(models.Model):

    #category,url,topic,description 





class Attendance(models.Model):

    #user_id(foreign key),#event_id(foreign key), attendance(String)



class Solutions(models.Model)
    #Task if ( foreign key), solution , submitted by(defaut shud be autehnticated user),date_of submission




'''




