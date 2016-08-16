from django.shortcuts import render

from .forms import ArticleForm
from .models import Article

def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
    else:
        form = ArticleForm()
    return render(request, 'summaries/index.html', {'form': form})