from django import forms

class ArticleForm(forms.Form):
    CHOICES = [('1', 'Read a random article'), ('2', 'Read n random articles'), 
                ('3', 'Read random articles until I\'m bored')]
    options = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)