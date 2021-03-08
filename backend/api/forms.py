from django import forms

class NewsTitlesForm(forms.Form):
	first_title = forms.CharField(max_length=25)
	second_title = forms.CharField(max_length=25)
	third_title = forms.CharField(max_length=25)
    