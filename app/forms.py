from django import forms
from app.models import *
class topicForm(forms.ModelForm):
    class Meta:
        model=topic
        fields='__all__'

class webpageForm(forms.ModelForm):
    class Meta:
        model=webpage
        fields='__all__'


class access_recordForm(forms.ModelForm):
    class Meta:
        model=access_record
        fields='__all__'
