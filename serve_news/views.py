from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article


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

    return render(request, 'news-view.html', {'articles': articles})
