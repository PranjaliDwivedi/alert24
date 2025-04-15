from django.shortcuts import render
from main.models import Categories,News

from .forms import Students

def search(request):
    query = request.GET.get('search')
    data = news.objects.filter(title__icontains = query)
    context = {
        'news': data
    }
    return render(request, 'search.html', context)


def home(request):
    category = Categories.objects.all()
    allnews = News.objects.all().order_by('-id')[:5]
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'cetegories': category,
        'allNews': allnews,
        'topNews': topNews}
    return render(request, 'index.html', context )

def india(request):
    category = Categories.objects.all()
    allNews = News.objects.filter(category__title='India News').order_by('-id')[:5]
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'cetegories': category,
        'allNews': allnews,
        'topNews': topNews
        }
    return render(request,'categories/india.html', context)

def bolly(request):
    category = Categories.objects.all()
    
    bollyNews = News.objects.filter(category__title='Bollywood News').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category, 
        'bollyNews': bollyNews,
        'topNews': topNews
        }
    return render(request, 'categories/bollywood.html', context)    

def detail(request, id):
    news = News.objects.get(pk = id )
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'news': news,
        'topNews': topNews
        }
    return render(request,'detail.html', context)


 
