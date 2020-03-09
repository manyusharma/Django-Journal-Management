from django.urls import path
from .views import *

app_name = "Journals"

urlpatterns = [
				path("<int:id>/edit/", journal_edit, name="edit"),
				path("all/", journals_all, name="all"),
				path("<int:id>/", fetch_by_id, name="by_id"),  
				path("new/", journal_new, name="new"),
				path("<slug:inp_slug>/", fetch_by_slug, name="by_slug"),
                path("<slug:inp_slug>/delete/", journal_delete, name="del"),
			  ]