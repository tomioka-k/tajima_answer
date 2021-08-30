from django.db.models import fields
from django.forms import ModelForm
from .models import Question, Reply


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('classiffication', 'method', 'content')
        labels = {
            'classiffication': '大分類',
            'method': '工法分類',
            'content': '質問内容',
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('content',)