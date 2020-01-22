from django.contrib import admin

from .models import UserMessage


class UserMessageAdmin (admin.ModelAdmin):
    list_display = ('name', 'send_date', 'email', 'subject')


admin.site.register(UserMessage, UserMessageAdmin)
# Register your models here.
