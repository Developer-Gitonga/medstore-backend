from django import forms
from .models import Donating


class DonatingForm(forms.ModelForm):
		class Meta:
			model = Donating
			exclude = ['donor'] 