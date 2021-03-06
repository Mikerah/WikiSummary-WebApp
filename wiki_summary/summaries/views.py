from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages 

from .forms import ArticleForm
from .models import Article

import wikipedia

def get_wanted_article(article):
    article_page = wikipedia.WikipediaPage(article)
    wanted_article_model = Article(
        title = article_page.title,
        content = article_page.summary,
        full_article = article_page.url
    )
    return wanted_article_model
    
def get_wanted_articles(number_of_articles):
    list_of_articles = []
    for i in range(number_of_articles):
        try:
            rand_article = wikipedia.random()
            page = wikipedia.WikipediaPage(rand_article)
            article = Article(
                title = page.title,
                content = page.summary,
                full_article = page.url
            )
            list_of_articles.append(article)
        except wikipedia.exceptions.DisambiguationError:
            rand_article = wikipedia.random()
    return list_of_articles
    
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
                request.session['number_of_articles'] = number_of_art
                return HttpResponseRedirect('/articles.html')
            
    else:
        form = ArticleForm()
    return render(request, 'summaries/index.html', {'form': form})
    
def article(request):
    article_title = request.session['wanted_article']
    wanted_article = get_wanted_article(article_title)
    return render(request, 'summaries/article.html', {'article': wanted_article})
    
def articles(request):
    number_of_articles = request.session['number_of_articles']
    articles = get_wanted_articles(number_of_articles)
    return render(request, 'summaries/articles.html', {'articles': articles, 'number_of_articles': range(number_of_articles)})
    
    