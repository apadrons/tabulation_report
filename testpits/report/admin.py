from django.contrib import admin

from .models import Report,Project

class ReportAdmin(admin.ModelAdmin):
    list_display = ['test_pit', 'project_number', 'date_project']

# Register your models here.
admin.site.register(Project)
admin.site.register(Report,ReportAdmin)

