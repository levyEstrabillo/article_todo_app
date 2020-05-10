from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(response):
    articles = models.Article.objects.all().order_by('date')
    return render(response, 'articles/article_list.html', {'articles': articles})

@login_required(login_url='accounts:login')
def article_detail(response, id):
    article = models.Article.objects.get(id=id)
    return render(response, 'articles/article_detail.html', {'article': article})
    

@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()            
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})


def article_delete(request, id):
    if request.method == 'POST':
        article = models.Article.objects.get(id=id)
        article.delete()
        return redirect('articles:list')



'''def article_edit(request, id):
    article = models.Article.objects.get(id=id)
    if request.method == 'POST':
        return HttpResponse(request.POST['title'])
    else:
    return render(request, 'articles/article_edit.html', {'article': article})

'''    