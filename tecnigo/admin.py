from django.contrib import admin
from tecnigo.models import TecnicalSupportStaff

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('FIRST_NAME', 'LAST_NAME') 
    pass

admin.site.register(TecnicalSupportStaff, AuthorAdmin)

