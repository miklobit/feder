from django.contrib import admin

from .models import Monitoring


class MonitoringAdmin(admin.ModelAdmin):
    '''
        Admin View for Monitoring
    '''
    list_display = ('name', 'user')
    search_fields = ['name']
admin.site.register(Monitoring, MonitoringAdmin)
