from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News, Ad, LikePage

def index(request):
    return render(request, 'index.html')

class NewsListView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-date']


class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'


class Ads(ListView):
    model = Ad
    template_name = 'ads.html'
    context_object_name = 'ads'
    ordering = ['-date_create']


class AdsDetail(DetailView):
    model = Ad
    template_name = 'ads_detail.html'
    context_object_name = 'ads_detail'


class AdPrivatePage(ListView):
    model = Ad
    template_name = 'ads_private.html'
    context_object_name = 'ads'
    ordering = ['-date_create']


class AdPrivateDetail(DetailView):
    model = Ad
    template_name = 'ads_private_detail.html'
    context_object_name = 'ads_detail'


class AdLike(DetailView):
    model = LikePage
    template_name = 'ads_like.html'
    context_object_name = 'ads_like'
