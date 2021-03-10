from django import forms

class NewsTitlesForm(forms.Form):
	first_title = forms.CharField(max_length=200)
	second_title = forms.CharField(max_length=200)
	third_title = forms.CharField(max_length=200)
    