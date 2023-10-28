from django.forms import ModelForm
from .models import Sportnews, Coment


class NewsForm(ModelForm):
    class Meta:
        model = Sportnews
        fields = ['tsport', 'title', 'news', 'image']

        labels = {
            'tsport': 'Тема новости',
            'title': 'Введите заголовок',
            'news': 'Введите текст статьи',
            'image': 'Загрузите изображение'
        }


class ComentForm(ModelForm):
    class Meta:
        model = Coment
        fields = ['value', 'body']

        labels = {
            'value': 'Ваша оценка статьи',
            'body': 'Введите ваш комментарий'
        }
