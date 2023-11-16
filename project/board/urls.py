from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('ads/', Ads.as_view(), name='ads'),
    path('ads/<int:pk>/', AdsDetail.as_view(), name='ads_detail'),
    path('adsprivate/', AdPrivatePage.as_view(), name='adsprivate'),
    path('adsprivate/<int:pk>/', AdPrivateDetail.as_view(), name='adprivatedetail'),
    path('adlike/', AdLike.as_view(), name='adlike'),
]