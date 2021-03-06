''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "4.0" 
__created__     =       "12/18/2019 08:50" 
''' 


from .models import Item
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):

	list_display = (
		'item_id',
		'item_name',
		'item_image',
		'item_bool',
		'item_date',
		'item_update_date',
		'item_date_auto',
		'item_update_date_auto',
		'item_decimal',
		'item_email',
		'item_file',
		'item_integer',
		'item_slug',
		'item_url',
		'item_uuid',
		'item_text',
		'item_choices',
	)
	list_editable = (
		'item_name',
		'item_image',
		'item_bool',
		'item_date',
		'item_update_date',
		'item_decimal',
		'item_email',
		'item_file',
		'item_integer',
		'item_slug',
		'item_url',
		'item_text',
		'item_choices',
	)
	list_filter = (
		'item_id',
		'item_name',
		'item_image',
		'item_bool',
		'item_date',
		'item_update_date',
		'item_date_auto',
		'item_update_date_auto',
		'item_decimal',
		'item_email',
		'item_file',
		'item_integer',
		'item_slug',
		'item_url',
		'item_uuid',
		'item_text',
		'item_choices',
	)
	search_fields = (
		'item_id',
		'item_name',
		'item_image',
		'item_bool',
		'item_date',
		'item_update_date',
		'item_date_auto',
		'item_update_date_auto',
		'item_decimal',
		'item_email',
		'item_file',
		'item_integer',
		'item_slug',
		'item_url',
		'item_uuid',
		'item_text',
		'item_choices',
	)


admin.site.register(Item, ItemAdmin)