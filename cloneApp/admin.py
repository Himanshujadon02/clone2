from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','number')

admin.site.register(Popular_blogs)
admin.site.register(Why_netcore)
admin.site.register(About)
admin.site.register(Our_involvement)
admin.site.register(Testonomial)
admin.site.register(Logo)
# admin.site.register(Landing)