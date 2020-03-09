from django import forms
from django.contrib.auth import get_user_model

# retrieves the current admin user model
User = get_user_model() 
class UserRegistration(forms.ModelForm):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
					"username",
					"email", 
					"password",
					"confirm_password"
				 ]

	def clean_email(self, *args, **kwargs):
		user_email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=user_email)
		if qs.exists():
			raise forms.ValidationError("email already taken")

		return user_email

	def clean_confirm_password(self, *args, **kwargs):
		password = self.cleaned_data.get("password")
		c_password = self.cleaned_data.get("confirm_password")
		if password != c_password:
			raise forms.ValidationError("Passwords do not match")

		return c_password




class UserLogin(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		fields = [
				  "username", 
				  "password"
				 ]