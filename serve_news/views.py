from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Article
from get_news.parser import parse


# Create your views here.
def news(request):

    articles = Article.objects.values()
    page = request.GET.get('page', 1)

    paginator = Paginator(articles, 10)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'articles': articles})


def test(request):
    data = parse()

    return render(request, 'test.html', {'data': data})

