from pyexpat import model
from .models import Complain, Comment, CommentByTeacher,Status
from django import forms


class CreateComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = '__all__'
        exclude = ['author', 'liked', 'same']

        labels = {
            'suggestions': 'Suggestions:(Split Your Suggestions by Comma)',
        }
        widgets = {

            'suggestions': forms.Textarea(attrs={'placeholder': "Ex:Replace that man with another suitable Person, Change All Defected Speakers", }),


        }

class StatusChangedForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        exclude = ['post',]


        