from django import forms
from .models import *


class QuestionForm(forms.Form):
    answer = forms.CharField()


class BasuForm1(forms.Form):
    answer1 = forms.CharField(help_text='Answer 1')
    answer2 = forms.CharField(help_text='Answer 2')