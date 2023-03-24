from django.urls import path

from frontend.api import views

urlpatterns = [
    path('graphics-cards/en/', views.IndexView.as_view(), name='index'),
    path(r'graphics-cards/en/<c_val_1>-vs-<c_val_2>/', views.CompareView.as_view(), name='compare'),
    path(r'graphics-cards/en/<selected>/', views.DetailView.as_view(), name='detail'),

    path('graphics-cards/ar/', views.ArIndexView.as_view(), name='index'),
    path(r'graphics-cards/<c_val_1>-vs-<c_val_2>/ar/', views.ArCompareView.as_view(), name='compare'),
    path(r'graphics-cards/<selected>/en/', views.ArDetailView.as_view(), name='detail'),

    path('graphics-cards/de/', views.DeIndexView.as_view(), name='index'),
    path(r'graphics-cards/de/<c_val_1>-vs-<c_val_2>/', views.DeCompareView.as_view(), name='compare'),
    path(r'graphics-cards/de/<selected>/', views.DeDetailView.as_view(), name='detail'),

    path('graphics-cards/es/', views.EsIndexView.as_view(), name='index'),
    path(r'graphics-cards/es/<c_val_1>-vs-<c_val_2>/', views.EsCompareView.as_view(), name='compare'),
    path(r'graphics-cards/es/<selected>/', views.EsDetailView.as_view(), name='detail'),

    path('graphics-cards/fr/', views.FrIndexView.as_view(), name='index'),
    path(r'graphics-cards/fr/<c_val_1>-vs-<c_val_2>/', views.FrCompareView.as_view(), name='compare'),
    path(r'graphics-cards/fr/<selected>/', views.FrDetailView.as_view(), name='detail'),

    path('graphics-cards/hi/', views.HiIndexView.as_view(), name='index'),
    path(r'graphics-cards/hi/<c_val_1>-vs-<c_val_2>/', views.HiCompareView.as_view(), name='compare'),
    path(r'graphics-cards/hi/<selected>/', views.HiDetailView.as_view(), name='detail'),

    path('graphics-cards/id/', views.IdIndexView.as_view(), name='index'),
    path(r'graphics-cards/<c_val_1>-vs-<c_val_2>/id/', views.IdCompareView.as_view(), name='compare'),
    path(r'graphics-cards/<selected>/id/', views.IdDetailView.as_view(), name='detail'),

    path('graphics-cards/it/', views.ItIndexView.as_view(), name='index'),
    path(r'graphics-cards/<c_val_1>-vs-<c_val_2>/it/', views.ItCompareView.as_view(), name='compare'),
    path(r'graphics-cards/<selected>/it/', views.ItDetailView.as_view(), name='detail'),

    path('graphics-cards/ja/', views.JaIndexView.as_view(), name='index'),
    path(r'graphics-cards/<c_val_1>-vs-<c_val_2>/ja/', views.JaCompareView.as_view(), name='compare'),
    path(r'graphics-cards/<selected>/ja/', views.JaDetailView.as_view(), name='detail'),

    path('graphics-cards/ko/', views.KoIndexView.as_view(), name='index'),
    path(r'graphics-cards/<c_val_1>-vs-<c_val_2>/ko/', views.KoCompareView.as_view(), name='compare'),
    path(r'graphics-cards/<selected>/ko/', views.KoDetailView.as_view(), name='detail'),

    path('graphics-cards/pl/', views.PlIndexView.as_view(), name='index'),
    path(r'graphics-cards/<c_val_1>-vs-<c_val_2>/pl/', views.PlCompareView.as_view(), name='compare'),
    path(r'graphics-cards/<selected>/pl/', views.PlDetailView.as_view(), name='detail'),

    path('graphics-cards/pt/', views.PtIndexView.as_view(), name='index'),
    path(r'graphics-cards/<c_val_1>-vs-<c_val_2>/pt/', views.PtCompareView.as_view(), name='compare'),
    path(r'graphics-cards/<selected>/pt/', views.PtDetailView.as_view(), name='detail'),

    path('graphics-cards/ru/', views.RuIndexView.as_view(), name='index'),
    path(r'graphics-cards/<c_val_1>-vs-<c_val_2>/ru/', views.RuCompareView.as_view(), name='compare'),
    path(r'graphics-cards/<selected>/ru/', views.RuDetailView.as_view(), name='detail'),

    path('graphics-cards/tr/', views.TrIndexView.as_view(), name='index'),
    path(r'graphics-cards/tr/<c_val_1>-vs-<c_val_2>/', views.TrCompareView.as_view(), name='compare'),
    path(r'graphics-cards/tr/<selected>/', views.TrDetailView.as_view(), name='detail'),

    path('graphics-cards/zh/', views.ZhIndexView.as_view(), name='index'),
    path(r'graphics-cards/zh/<c_val_1>-vs-<c_val_2>/', views.ZhCompareView.as_view(), name='compare'),
    path(r'graphics-cards/zh/<selected>/', views.ZhDetailView.as_view(), name='detail'),
]
