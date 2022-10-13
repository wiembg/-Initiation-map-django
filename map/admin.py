from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import AllData


class DataImportExportAdmin(ImportExportModelAdmin):
    list_display = ('Indicator', 'Country', 'ADM1_CODE', 'Province' )


admin.site.register(AllData, DataImportExportAdmin)