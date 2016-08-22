from django import forms

class ArticleForm(forms.Form):
    CHOICES = [(1, 'Read an article'), (2, 'Read n random articles')]
    options = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id': 'selections'}), required=True)
    specific_article = forms.CharField(max_length=250, required=False, widget=forms.TextInput(), label=("Specific Article"))
    number_of_random_articles = forms.IntegerField(required=False, widget=forms.NumberInput(), label=("Number of Articles"), initial=5)
    
    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        selection = cleaned_data.get("options")
        if selection == "1":
            specific_article = cleaned_data.get("specific_article")
            if specific_article == "":
                raise forms.ValidationError("Please Enter an Article")