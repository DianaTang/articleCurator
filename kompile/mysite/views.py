# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.http import Http404

from .models import Article

def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:5]
    context = {
        'latest_articles': latest_articles,
    }
    return render(request, 'mysite/index.html', context)

def detail(request, article_id):
    article = get_object_or_404 (Article, pk=article_id)
    return render (request, 'mysite/detail.html', {'article': article})

def category_filter(request, category_id):
    response = "You're looking at the results of category %s."
    return HttpResponse(response % category_id)
