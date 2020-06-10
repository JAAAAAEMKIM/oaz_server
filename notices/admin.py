from django.contrib import admin
from notices.models import Notice

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    model = Notice

admin.site.register(Notice, NoticeAdmin)