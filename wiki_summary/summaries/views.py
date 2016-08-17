from django.shortcuts import render

from .forms import ArticleForm
from .models import Article

def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            selection = form.cleaned_data['options']
        
    else:
        form = ArticleForm()
    return render(request, 'summaries/index.html', {'form': form})