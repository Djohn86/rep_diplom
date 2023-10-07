from django.forms import ModelForm
from .models import Sportnews


class NewsForm(ModelForm):
    class Meta:
        model = Sportnews
        fields = ['tsport', 'title', 'news']
