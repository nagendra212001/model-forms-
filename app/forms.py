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
        #fields=['topic_name','name']
        #exclude=['name']
        help_texts={'topic_name':'should not be integers','name':'only Alphabets'}
        labels={'topic_name':'TN','name':'N'}
        widgets={'url':forms.PasswordInput,'name':forms.Textarea}
    


class access_recordForm(forms.ModelForm):
    class Meta:
        model=access_record
        fields='__all__'
