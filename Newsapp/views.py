from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.


def index(request):
    newsapi = NewsApiClient(api_key="ff61f6a2a5e24b92b6dbc8065a98b350")
    topheadline = newsapi.get_top_headlines(sources='al-jazeera-english')

    articles = topheadline['articles']
    desc = []
    news =[]
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news,desc,img)

    return render(request,'index.html',context={'mylist':mylist})


def bbc(request):
    newsapi = NewsApiClient(api_key="ff61f6a2a5e24b92b6dbc8065a98b350")
    topheadline = newsapi.get_top_headlines(sources='bbc-news')

    articles = topheadline['articles']
    desc = []
    news =[]
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news,desc,img)

    return render(request,'bbc.html',context={'mylist':mylist})


def times(request):
    newsapi = NewsApiClient(api_key="ff61f6a2a5e24b92b6dbc8065a98b350")
    topheadline = newsapi.get_top_headlines(sources='the-times-of-india')

    articles = topheadline['articles']
    desc = []
    news =[]
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news,desc,img)

    return render(request,'times.html',context={'mylist':mylist})


def espn(request):
    newsapi = NewsApiClient(api_key="ff61f6a2a5e24b92b6dbc8065a98b350")
    topheadline = newsapi.get_top_headlines(sources='espn-cric-info')

    articles = topheadline['articles']
    desc = []
    news =[]
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news,desc,img)

    return render(request,'espn.html',context={'mylist':mylist})


def yent(request):
    newsapi = NewsApiClient(api_key="ff61f6a2a5e24b92b6dbc8065a98b350")
    topheadline = newsapi.get_top_headlines(sources='ynet')

    articles = topheadline['articles']
    desc = []
    news =[]
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news,desc,img)

    return render(request,'ynet.html',context={'mylist':mylist})


def lenta(request):
    newsapi = NewsApiClient(api_key="ff61f6a2a5e24b92b6dbc8065a98b350")
    topheadline = newsapi.get_top_headlines(sources='lenta')

    articles = topheadline['articles']
    desc = []
    news =[]
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip((news,desc,img))

    return render(request,'lenta.html',context={'mylist':mylist})