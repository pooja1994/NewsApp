from django.shortcuts import render
from account.models import Account
import requests

API_KEY = '129681b8de26458eafdff21e42c203f6'


# Create your views here.
def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country is not None:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category is not None:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    context = {
        'articles': articles
    }
    return render(request, 'news_api/home.html', context)


def search_news(request):
    search_list = '{}'
    keyword = request.GET.get('q')
    category = request.GET.get('category')

    if keyword is not None and keyword != '':
        datePublished = request.GET.get('publishedAt')
        name = request.GET.get('name')
        language = request.GET.get('language')
        d = ''
        n = ''
        l = ''
        if datePublished is not None and datePublished != '':
            d = f'&from={datePublished}&to={datePublished}'
        if name is not None and name != '':
            n = f'&sources={name}'
        if language is not None and language != '':
            l = f'&language={language}'
        url = f'https://newsapi.org/v2/everything?q={keyword}{n}{d}{l}&apiKey={API_KEY}'
        r = requests.get(url)
        results = r.json()
        search_list = results['articles']

        if request.user.is_authenticated:
            username = request.user.username
            user_object = Account()
            ins = user_object.add_keyword(username, keyword)
            ins.save()

    context = {
        'search_list': search_list
    }
    return render(request, 'news_api/home.html', context)

