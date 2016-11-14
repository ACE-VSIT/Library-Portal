from django.contrib import admin

admin.site.site_title = 'ACE VIRTUAL LIBRARY'
admin.site.site_header = 'ACE ADMIN PANEL'

<<<<<<< HEAD
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
=======
from .models import Tasks

# Register your models here.
admin.site.register(Tasks)
>>>>>>> 1eaccff4ddf20d6f6006902dcb5ebd5ec147acec
