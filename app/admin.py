from django.contrib import admin

# Register your models here.

from app.models import *

class webpageCustomView(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_editable=['name']
    list_display_links=['topic_name','url']
    #list_per_page=2
    search_fields=['name']
    list_filter=['name','topic_name']


admin.site.register(topic)

admin.site.register(webpage,webpageCustomView)

admin.site.register(access_record)