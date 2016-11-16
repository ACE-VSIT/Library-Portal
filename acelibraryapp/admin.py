from django.contrib import admin

admin.site.site_title = 'ACE VIRTUAL LIBRARY'
admin.site.site_header = 'ACE ADMIN PANEL'

from .models import Tasks,Resources, Categories, Event, Attendance

# Register your models here.
admin.site.register(Tasks)
#admin.site.register(Resources)
admin.site.register(Categories)
admin.site.register(Event)
admin.site.register(Attendance)

class SampleAdmin(admin.ModelAdmin):
	pass


class BookAdmin(admin.ModelAdmin):
    list_display = ('Category','Course','Author','URL', 'approval_status')

admin.site.register(Resources, BookAdmin)
