from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.db.models import Q



def index(request):
    latest_posts_list = Article.objects.order_by("-pub_time")[:5]
    categorys = Category.objects.all()
    context = {
        "latest_posts_list": latest_posts_list,
        "categorys": categorys,
    }
    return render(request, "helpdesk/index.html", context)


def article(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    categorys = Category.objects.all()
    context = {
        "article": article,
        "categorys": categorys,
    }
    return render(request, "helpdesk/article.html", context)


def search_articles(request):
    query = request.GET.get('q')
    categorys = Category.objects.all()
    results = Article.objects.filter(Q(name__icontains=query) | Q(body__icontains=query))
    context = {
        "results": results,
        "categorys": categorys,
        "query": query,
    }
    return render(request, "helpdesk/search.html", context)
