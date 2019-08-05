from django.forms import forms


class StoryForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    author = forms.ModelChoiceField()
