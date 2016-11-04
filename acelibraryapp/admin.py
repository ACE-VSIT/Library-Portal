from django.contrib import admin
from .models import Tasks,Student,User
from django.contrib import admin

admin.site.site_title = 'ACE VIRTUAL LIBRARY'
admin.site.site_header = 'ACE ADMIN PANEL'

# Register your models here.
'''
class UserInline(admin.StackedInline):

	model = User


class StudentAdmin(admin.ModelAdmin):

	fieldsets = [(None,{'fields': ['enroll_number']}),('Student information', {'fields': ['name','email_id'], 'classes': ['collapse']}),]

	inlines = [UserInline]


admin.site.register(Student,StudentAdmin)
'''

class AceAdmin(admin.ModelAdmin):
	save_on_top = True

	pass

admin.site.register(User)
