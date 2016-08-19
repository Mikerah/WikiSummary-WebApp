from django import forms

class ArticleForm(forms.Form):
    CHOICES = [(1, 'Read an article'), (2, 'Read n random articles')]
    options = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id': 'selections'}))
    specific_article = forms.CharField(max_length=250, required=False, widget=forms.TextInput(), label=("Specific Article"))
    number_of_random_articles = forms.IntegerField(required=False, widget=forms.NumberInput(), label=("Number of Articles"))