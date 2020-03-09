from django import forms
import datetime
from .models import Journal

class JournalForm(forms.ModelForm):
	publish = forms.CharField(widget=forms.SelectDateWidget,
							  initial=datetime.date.today)
	class Meta:
		model = Journal
		fields = [
					"title",
					"detail",
					"image",
					"publish"
				 ]