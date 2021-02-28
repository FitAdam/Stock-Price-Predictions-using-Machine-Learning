from django.forms import ModelForm
from . models import NewsTitles

class NewsTitlesForm(ModelForm):
	class Meta:
		model=NewsTitles
		fields = '__all__'