from django.contrib import admin

admin.site.site_title = 'ACE VIRTUAL LIBRARY'
admin.site.site_header = 'ACE ADMIN PANEL'

from .models import Tasks

# Register your models here.
admin.site.register(Tasks)
