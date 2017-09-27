from django import forms
from .models import *


class QuestionForm(forms.Form):
    answer = forms.CharField()