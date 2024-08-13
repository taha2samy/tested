
from django.contrib import admin
from .models import Provider, Consumer

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('username','pk')  

    def username(self, obj):
        return obj.user.username

class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('username','pk') 

    def username(self, obj):
        return obj.user.username

admin.site.register(Provider, ProviderAdmin)
admin.site.register(Consumer, ConsumerAdmin)
