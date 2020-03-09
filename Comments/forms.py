from .models import Comment
from django import forms

class CommentForm(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.CharField(widget=forms.HiddenInput)
	content = forms.CharField(widget=forms.Textarea)

	