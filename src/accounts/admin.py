from django.contrib import admin
from accounts.models import User,Profile,Address

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email","is_staff","is_owner")

admin.site.register(Profile)
admin.site.register(Address)
