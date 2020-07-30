from django.contrib import admin
from .models import deal
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class DealResource(resources.ModelResource):

    class Meta:
        model = deal
        exclude = ['id']

class DealAdmin(ImportExportModelAdmin):
    resource_class = DealResource
    list_display = [field.name for field in deal._meta.fields if field.name != "id"]
    pass

class dealAdmin(admin.ModelAdmin):
    list_display = [field.name for field in deal._meta.fields]

    class Meta:
        model = deal

# admin.site.register(deal, dealAdmin)
admin.site.register(deal, DealAdmin)
# Register your models here.
