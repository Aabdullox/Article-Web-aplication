from django.shortcuts import render
from article.models import Article

def index(request):
    articles = Article.objects.order_by('-id')[:4]
    sport_category_articles = Article.objects.filter(category='Game')[:3]
    all_categories = list (set(Article.objects.values_list('category', flat=True)))


    context = {
        "articles": articles,
        " sport_category_articles ": sport_category_articles,
        "all_categories": all_categories,
    }
    return render(request, "index.html", context)


def categories_page(request):
    cat = request.GET.get("cat")
    articles = Article.objects.filter(category=cat)
    all_categories = list(set(Article.objects.values_list('category', flat=True)))
    context = {
        "articles": articles,
        "cat": cat,
        "all_categories": all_categoris,
        "page": page
    }

    return render (request,'index.html', context=context)


def search_articles(request):
    search = request.GET.get("search")
    all_categories = list(search(Article.objects.values_list('category', flat=True)))


    if search:
        articles = Article.objects.filter(title__icontains=search)
    else:
        articles = Article.objects.all()
    context = {
        "articles": articles,
        "all_categories": all_categories
    }
    return render(request, ' search_articles.html', context=context)