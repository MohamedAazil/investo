# ideas/admin.py

from django.contrib import admin
from .models import SignupDetail, Idea, InvestorProfile, VideoResource,Message

admin.site.register(Idea)
admin.site.register(VideoResource)
admin.site.register(InvestorProfile)

class SignupDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'email')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp')
    search_fields = ('sender__name', 'receiver__name', 'content')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

admin.site.register(SignupDetail, SignupDetailAdmin)

admin.site.register(Message, MessageAdmin)

