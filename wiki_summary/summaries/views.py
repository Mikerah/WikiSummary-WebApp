from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ArticleForm
from .models import Article

import wikipedia

def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            selection = form.cleaned_data['options']
            if selection == '1':
                spec_article = form.cleaned_data['specific_article']
                request.session['wanted_article'] = spec_article[:]
                return HttpResponseRedirect('/article.html')
            elif selection == '2':
                number_of_art = form.cleaned_data['number_of_random_articles']
                request.session['number_of_articles'] = number_of_art[:]
                return HttpResponseRedirect('/articles.html')
            else:
                return HttpResponseRedirect('/infinite_articles.html')
                
    else:
        form = ArticleForm()
    return render(request, 'summaries/index.html', {'form': form})
    
def article(request):
    pass
    
def articles(request):
    pass
    
def infinite_articles(request):
    pass
    