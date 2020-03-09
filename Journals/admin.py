from django.contrib import admin

from .models import Journal

class JournalAdmin(admin.ModelAdmin):
	list_display = [
					"id",
					"title",
					"timestamp",
					"last_updated"
				   ]

	list_display_links = [
							"title",
							"timestamp"
						 ]

	list_filter = [
					"timestamp", 
					"last_updated"
				  ]

	search_fields = [ "title"]

admin.site.register(Journal, JournalAdmin)
