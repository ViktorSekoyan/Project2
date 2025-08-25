from django.contrib import admin
from .models import (
    Subscribe,headericon,Categoriesofthemonth,Categoryandfeature,
    heroandbrand,Shopsinglehtml,Shophtml,Letstalk
)
# Register your models here.

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email2','created_at']
    readonly_fields = ['email2','created_at']

class LetstalkAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','submitted_at']
    readonly_fields = ['name','email','subject','message','submitted_at']

admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(headericon)
admin.site.register(Categoriesofthemonth)
admin.site.register(Categoryandfeature)
admin.site.register(heroandbrand)
admin.site.register(Shopsinglehtml)
admin.site.register(Shophtml)
admin.site.register(Letstalk, LetstalkAdmin)