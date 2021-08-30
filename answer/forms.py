from django.forms import ModelForm
from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('classiffication', 'method', 'content')
        labels = {
            'classiffication': '大分類',
            'method': '工法分類',
            'content': '質問内容',
        }
