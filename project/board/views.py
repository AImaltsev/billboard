from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import News, Ad, LikePage, Category
from .forms import AdForm
from django.contrib.auth.decorators import login_required

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

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


@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.views = 0
            ad.save()
            return redirect('ads_detail', pk=ad.pk)
    else:
        form = AdForm()

    return render(request, 'create_ad.html', {'form': form})