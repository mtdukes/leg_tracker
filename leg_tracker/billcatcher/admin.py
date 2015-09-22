from django.contrib import admin

# Register your models here.
from .models import Lawmaker
from .models import Bill

class LawmakerAdmin(admin.ModelAdmin):
	list_display = ['name','chamber','party','county_short']

class BillAdmin(admin.ModelAdmin):
	list_display = ['title','bill_number','file_date', 'watch']
	search_fields = ['title', 'bill_number']
	list_filter = ['file_date', 'watch']
	readonly_fields = ('updated',)

admin.site.register(Lawmaker, LawmakerAdmin)
admin.site.register(Bill, BillAdmin)