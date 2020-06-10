from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserInfo
# from users.models import User

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    model = UserInfo

admin.site.register(User, UserAdmin)