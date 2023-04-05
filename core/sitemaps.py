from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import GPUSpecs

class GPUSpecsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return GPUSpecs.objects.all()

    # returns the URL of the article object
    def location(self, obj):
        return f'/graphics-cards/fr/{obj.gpu_url}'

    # def lastmod(self, obj):
    #     return obj.release_date

    def get_queryset(self, obj):
        return GPUSpecs.objects.filter(status=GPUSpecs.PUBLISHED)

class CompareGPUSpecsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        specs = GPUSpecs.objects.all()
        return [(spec1, spec2) for spec1 in specs for spec2 in specs if spec1 != spec2]

    def location(self, item):
        spec1, spec2 = item
        return f'/graphics-cards/fr/{spec1.gpu_url}-vs-{spec2.gpu_url}'
        # return reverse('compare_gpus', args=[spec1.slug, spec2.slug])

    # def lastmod(self, item):
    #     spec1, spec2 = item
    #     return max(spec1.updated, spec2.updated)


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['main:homepage_view', 'main:contact_view']

    def location(self, item):
        return reverse(item)
