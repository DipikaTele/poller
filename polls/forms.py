from django import forms
from polls import models

class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['choice']