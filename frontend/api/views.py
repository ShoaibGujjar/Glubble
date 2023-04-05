from django.views.generic.base import TemplateView
from core.models import GPUSpecs
from django.db.models import Q

class IndexView(TemplateView):
    template_name = 'en/index.html'

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data['data'] = GPUSpecs.objects.order_by('-performance')
        context_data['other_data'] = list(context_data['data'].values('id', 'performance'))
        return context_data


class CompareView(TemplateView):
    template_name = 'en/compare.html'

    def get_context_data(self, **kwargs):
        lang = self.template_name.split('/')[0]
        context_data = super(CompareView, self).get_context_data(**kwargs)
        context_data['data'] = GPUSpecs.objects.order_by('-performance')
        # context_data['data'] = GPUSpecs.objects.order_by('-performance').values('name', 'performance', 'price', 'year')
        q = Q()
        for d in [kwargs.get('c_val_1', ''), kwargs.get('c_val_2', '')]:
            q |= Q(name__icontains=d.replace('-', ' '))
        objs = GPUSpecs.objects.filter(q)
        for idx, obj in enumerate(objs):
            context_data[f'obj_{idx}'] = obj
            context_data[f'obj_{idx}_benchmark_performance'] = obj.benchmark_performance(lang)
        return context_data


class DetailView(TemplateView):
    template_name = 'en/info.html'

    def get_context_data(self, **kwargs):
        lang = self.template_name.split('/')[0]
        context_data = super(DetailView, self).get_context_data(**kwargs)
        context_data['data'] = GPUSpecs.objects.order_by('-performance')
        context_data['obj'] = GPUSpecs.objects.filter(name__iexact=kwargs.get('selected', '').replace('-', ' ').lower()).first()
        context_data[f'benchmark_performance'] = context_data['obj'].benchmark_performance(lang)
        return context_data


class ArDetailView(DetailView):
    template_name = 'ar/info.html'


class ArCompareView(CompareView):
    template_name = 'ar/compare.html'


class ArIndexView(IndexView):
    template_name = 'ar/index.html'


class DeDetailView(DetailView):
    template_name = 'de/info.html'


class DeCompareView(CompareView):
    template_name = 'de/compare.html'


class DeIndexView(IndexView):
    template_name = 'de/index.html'


class EsDetailView(DetailView):
    template_name = 'es/info.html'


class EsCompareView(CompareView):
    template_name = 'es/compare.html'


class EsIndexView(IndexView):
    template_name = 'es/index.html'


class FrDetailView(DetailView):
    template_name = 'fr/info.html'


class FrCompareView(CompareView):
    template_name = 'fr/compare.html'


class FrIndexView(IndexView):
    template_name = 'fr/index.html'
    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data['data'] = GPUSpecs.objects.order_by('-performance')
        context_data['obj'] = GPUSpecs.objects.get(performance=100) #performance__gt=self.performance
        context_data['other_data'] = list(context_data['data'].values('id', 'performance'))
        return context_data

class HiDetailView(DetailView):
    template_name = 'hi/info.html'


class HiCompareView(CompareView):
    template_name = 'hi/compare.html'


class HiIndexView(IndexView):
    template_name = 'hi/index.html'


class IdDetailView(DetailView):
    template_name = 'id/info.html'


class IdCompareView(CompareView):
    template_name = 'id/compare.html'


class IdIndexView(IndexView):
    template_name = 'id/index.html'


class ItDetailView(DetailView):
    template_name = 'it/info.html'


class ItCompareView(CompareView):
    template_name = 'it/compare.html'


class ItIndexView(IndexView):
    template_name = 'it/index.html'


class JaDetailView(DetailView):
    template_name = 'ja/info.html'


class JaCompareView(CompareView):
    template_name = 'ja/compare.html'


class JaIndexView(IndexView):
    template_name = 'ja/index.html'


class KoDetailView(DetailView):
    template_name = 'ko/info.html'


class KoCompareView(CompareView):
    template_name = 'ko/compare.html'


class KoIndexView(IndexView):
    template_name = 'ko/index.html'


class PlDetailView(DetailView):
    template_name = 'pl/info.html'


class PlCompareView(CompareView):
    template_name = 'pl/compare.html'


class PlIndexView(IndexView):
    template_name = 'pl/index.html'


class PtDetailView(DetailView):
    template_name = 'pt/info.html'


class PtCompareView(CompareView):
    template_name = 'pt/compare.html'


class PtIndexView(IndexView):
    template_name = 'pt/index.html'


class RuDetailView(DetailView):
    template_name = 'ru/info.html'


class RuCompareView(CompareView):
    template_name = 'ru/compare.html'


class RuIndexView(IndexView):
    template_name = 'ru/index.html'


class TrDetailView(DetailView):
    template_name = 'tr/info.html'


class TrCompareView(CompareView):
    template_name = 'tr/compare.html'


class TrIndexView(IndexView):
    template_name = 'tr/index.html'


class ZhDetailView(DetailView):
    template_name = 'zh/info.html'


class ZhCompareView(CompareView):
    template_name = 'zh/compare.html'


class ZhIndexView(IndexView):
    template_name = 'zh/index.html'
