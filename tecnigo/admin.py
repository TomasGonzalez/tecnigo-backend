from django.contrib import admin
from tecnigo.models import TecnicalSupportStaff

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    pass


admin.site.register(TecnicalSupportStaff, AuthorAdmin)
