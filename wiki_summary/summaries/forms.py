from django import forms

class ArticleForm(forms.Form):
    CHOICES = [(1, 'Read an article'), (2, 'Read n random articles'), 
                (3, 'Read random articles until I\'m bored')]
    options = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id': 'options'}))
    specific_article = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={'id': 'spec_art'}))
    number_of_random_articles = forms.IntegerField(max_value=10, required=False, widget=forms.NumberInput(attrs={'id': 'num_art'}))