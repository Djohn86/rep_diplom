from django.forms import ModelForm
from .models import Sportnews, Coment


class NewsForm(ModelForm):
    class Meta:
        model = Sportnews
        fields = ['tsport', 'title', 'news', 'image']


class ComentForm(ModelForm):
    class Meta:
        model = Coment
        fields = ['value', 'body']

        labels = {
            'value': 'Ваша оценка статьи',
            'body': 'Введите ваш комментарий'
        }
