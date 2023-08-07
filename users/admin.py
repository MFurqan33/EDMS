from django.contrib import admin
from users.models import UserDetail
# Register your models here.

class UserDetailAdmin(admin.ModelAdmin):
    list_display=('user','phone_number',)
    search_fields=('user__username',)


admin.site.register(UserDetail,UserDetailAdmin)


    