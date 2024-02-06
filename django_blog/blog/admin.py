from django.contrib import admin
from .models import Record

class PostModelAdmin(admin.ModelAdmin):
    admin.site.register(Record)