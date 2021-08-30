from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField

from accounts.models import User


class Classiffication(models.Model):
    """"""
    name = models.CharField(verbose_name='分類名', max_length=255, unique=True,)
    order = models.IntegerField(verbose_name='並び順', unique=True)
    created_at = models.DateField(verbose_name='作成日', default=timezone.now)
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.name


class Method(models.Model):
    """"""
    name = models.CharField(verbose_name='工法名名', max_length=255, unique=True,)
    order = models.IntegerField(verbose_name='並び順', unique=True)
    created_at = models.DateField(verbose_name='作成日', default=timezone.now)
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.name


class Question(models.Model):
    """"""
    classiffication = models.ForeignKey(
        Classiffication, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    content = MDTextField(verbose_name='質問内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="作成日", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="更新日", auto_now=True)
    resolve = models.BooleanField(default=False)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.content


class Reply(models.Model):
    """"""
    question = models.ForeignKey(
        Question, related_name='replies', on_delete=models.CASCADE)
    content = MDTextField(verbose_name='回答内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="作成日", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="更新日", auto_now=True)
    is_best_answer = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.content
