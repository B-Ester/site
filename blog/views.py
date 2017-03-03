from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from blog.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib import auth


def home(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles ,
           }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html' , { 'article' : article , 'username': auth.get_user(request).username })

def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id = article_id)
            article.likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

