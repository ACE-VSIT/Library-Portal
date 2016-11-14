from django.contrib import admin

admin.site.site_title = 'ACE VIRTUAL LIBRARY'
admin.site.site_header = 'ACE ADMIN PANEL'

from .models import Tasks,Resources, Categories

# Register your models here.
admin.site.register(Tasks)
#admin.site.register(Resources)
admin.site.register(Categories)

class SampleAdmin(admin.ModelAdmin):
	pass


class BookAdmin(admin.ModelAdmin):
    list_display = ('Category','Course','Author','Difficulty','URL', 'approval_status')

admin.site.register(Resources, BookAdmin)
