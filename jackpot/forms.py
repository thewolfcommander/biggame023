from django import forms
from .models import GameJackpot

class GameJackpotForm(forms.ModelForm):
	bet = forms.IntegerField(help_text = None, widget = forms.TextInput(attrs = {'placeholder': 'Select Bet'}))
	amount_for_bet = forms.DecimalField()
	spin = forms.BooleanField()

	class Meta:
		model = GameJackpot
		fields = ('bet', 'amount_for_bet', 'spin')