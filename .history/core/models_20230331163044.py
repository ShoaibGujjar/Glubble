import json

from django.db import models

from frontend.translation_util import get_translated_test_description


class GPUSpecs(models.Model):
    url = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    performance = models.FloatField(null=True, blank=True, default=0.0)
    year = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0.0)
    currency = models.CharField(max_length=255, null=True, blank=True, default='USD')
    general_info = models.JSONField(null=True, blank=True, default=list)
    technical_specs = models.JSONField(null=True, blank=True, default=list)
    compatibility_dimensions_requirements = models.JSONField(null=True, blank=True, default=list)
    memory = models.JSONField(null=True, blank=True, default=list)
    video_outputs_ports = models.JSONField(null=True, blank=True, default=list)
    technologies = models.JSONField(null=True, blank=True, default=list)
    api_support = models.JSONField(null=True, blank=True, default=list)
    tests = models.JSONField(null=True, blank=True, default=list)
    fps = models.JSONField(null=True, blank=True, default=list)
    relative_performance = models.JSONField(null=True, blank=True, default=list)
    equivalent_gpu = models.JSONField(null=True, blank=True, default=list)
    similar_gpu = models.JSONField(null=True, blank=True, default=list)
    rec_processor = models.JSONField(null=True, blank=True, default=list)
    presets = models.JSONField(null=True, blank=True, default=list)
    games = models.JSONField(null=True, blank=True, default=list)
    graph_html = models.TextField(null=True, blank=True)
    amzn_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name} -- {self.year} -- {self.price} {self.currency}"

    @classmethod
    def bulk_create_from_file(cls, filename):
        # file = open(filename)
        file = open(filename, encoding='UTF8')
        # returns JSON object as
        # a dictionary
        data = json.load(file)
        to_create = []
        key_map = {
            'compatibility, dimensions and requirements': 'compatibility_dimensions_requirements'
        }
        for d in data:
            d['price'] = d['price'].replace(' USD', '')
            try:
                int(d['price'])
            except Exception:
                d['price'] = 0
            try:
                int(d['year'])
            except Exception:
                d['year'] = 0
            try:
                float(d['performance'])
            except Exception:
                d['performance'] = 0

            to_create.append(
                cls(
                    **{
                        key_map.get(key, key): val
                        for key, val in d.items()
                    }
                )
            )
        cls.objects.bulk_create(to_create)

    @property
    def supplementary_power_connectors(self):
        if self.compatibility_dimensions_requirements:
            return self.compatibility_dimensions_requirements[0].get('Supplementary power connectors', '-')
        return '-'

    @property
    def chip_lithography(self):
        return '-'

    @property
    def generation(self):
        return ' '.join(self.name.split(' ')[1:])

    @property
    def market_segment(self):
        if self.general_info:
            return self.general_info[0].get('Market segment', '-')
        return '-'

    @property
    def gpu_code_name(self):
        if self.general_info:
            return self.general_info[0].get('GPU code name', '-')
        return '-'

    @property
    def architecture(self):
        if self.general_info:
            return self.general_info[0].get('Architecture', '-')
        return '-'

    @property
    def memory_size(self):
        if self.memory:
            return self.memory[0].get('Maximum RAM amount', '-')
        return '-'

    @property
    def memory_type(self):
        if self.memory:
            return self.memory[0].get('Memory type', '-')
        return '-'

    @property
    def memory_bus_width(self):
        if self.memory:
            return self.memory[0].get('Memory bus width', '-')
        return '-'

    @property
    def memory_clock_speed(self):
        if self.memory:
            return self.memory[0].get('Memory clock speed', '-')
        return '-'

    @property
    def memory_bandwidth(self):
        if self.memory:
            return self.memory[0].get('Memory bandwidth', '-')
        return '-'

    @property
    def core_clock_speed(self):
        if self.technical_specs:
            return self.technical_specs[0].get('Core clock speed', '-')
        return '-'

    @property
    def thermal_design_power(self):
        if self.technical_specs:
            return self.technical_specs[0].get('Thermal design power (TDP)', '-')
        return '-'

    @property
    def manufacturing_process_technology(self):
        if self.technical_specs:
            return self.technical_specs[0].get('Manufacturing process technology', '-')
        return '-'

    @property
    def number_of_transistors(self):
        if self.technical_specs:
            return self.technical_specs[0].get('Number of transistors', '-')
        return '-'

    @property
    def boost_clock_speed(self):
        if self.technical_specs:
            return self.technical_specs[0].get('Boost clock speed', '-')
        return '-'

    @property
    def cuda_cores(self):
        if self.technical_specs:
            return self.technical_specs[0].get('Pipelines / CUDA cores', '-')
        return '-'

    @property
    def all_tests(self):
        if self.tests:
            return [list(test.keys())[0] for test in self.tests[1:] if list(test.keys())]
        return []

    @property
    def full_hd(self):
        if self.fps:
            return self.fps[0].get('Full HD', '-')
        return '-'

    @property
    def r_1440p(self):
        if self.fps:
            return self.fps[0].get('1440p', '-')
        return '-'

    @property
    def r_4k(self):
        if self.fps:
            return self.fps[0].get('4K', '-')
        return '-'

    @property
    def all_presets(self):
        if self.presets:
            return [{'name': list(preset[0].items())[0][0], 'value': list(preset[0].items())[0][1]} for preset in list(self.presets[0].values())]
        return []

    @property
    def game_features(self):
        if self.presets[0]:
            return self.presets[0].keys()
        return []

    def all_games(self):
        if self.games:
            return [g['name'] for g in self.games]
        return

    def game_bar_chart(self):
        if self.games:
            return self.games[0]['graph_html']
        return ''


    @property
    def release_date(self):
        if self.general_info:
            return self.general_info[0].get('Release date', '-')
        return '-'
    
    @property
    def texture_fill_rate(self):
        if self.general_info:
            return self.technical_specs[0].get('Texture fill rate', '-')
        return '-'

    @property
    def url_name(self):
        return self.name.replace(' ', '-')

    def benchmark_performance(self, lang='en'):
        if self.tests:
            return [dict(name=list(data.keys())[0], score=list(data.values())[0], text=get_translated_test_description(list(data.keys())[0], lang)) for data in self.tests]
        return []

    @property
    def all_presets_data(self):
        data = {}
        if self.presets:
            for feature, games in self.presets[0].items():
                data.update(
                    {
                        feature: [{'name': game_name, 'score': rate} for game_name, rate in games[0].items()]
                    }
                )
        return data

    @property
    def relative_performance_data(self):
        if self.relative_performance:
            return [score for _, score in self.relative_performance[0].items()]
        return []

    @property
    def relative_performance_names(self):
        if self.relative_performance:
            return [name for name, _ in self.relative_performance[0].items()]
        return []

    @property
    def equivalent_gpu_data(self):
        if self.equivalent_gpu:
            return [score for _, score in self.equivalent_gpu[0].items()]
        return []

    @property
    def equivalent_gpu_names(self):
        if self.equivalent_gpu:
            return [name for name, _ in self.equivalent_gpu[0].items()]
        return []

    @property
    def equivalent_gpu_url_names(self):
        if self.equivalent_gpu:
            return [dict(name=name, url_name=name.replace(' ', '-').lower()) for name, _ in self.equivalent_gpu[0].items()]
        return []

    @property
    def similar_gpu_processes(self):
        data = list()
        if self.similar_gpu and self.rec_processor:
            for card, process in zip(self.similar_gpu, self.rec_processor):
                data.append(dict(name=card, processor=process))
        return data
    



    # @property
    # def compare_gpu(self,value):
    #     compare_data=list()
    #     # self.id
    #     if self.id:
    #         return [name for name, _ in self.equivalent_gpu[0].items()]
    #     return []

    #     return compare_data

    # @property
    # def first_20_instances(self):
    #     name1
    #     name2
    #     url
    #     image1
    #     image2
    #     return GPUSpecs.objects.all()[:20]
    @property
    def first_20_instances(self):
        instances = GPUSpecs.objects.all()[:20]
        for i, instance in enumerate(instances):
            if i < 19:
                instance.next_instance = instances[i+1]
            else:
                try:
                    instance.next_instance = GPUSpecs.objects.all()[20]
                except IndexError:
                    instance.next_instance = None
        
        # url1=instance.name.replace(' ', '-')
        # # url2=instance.next_instance.replace(' ', '-')
        # url=f"{url1}-vs-{url2}"
        # instances.append(url=url)
# return f"{self.name} -- {self.year} -- {self.price} {self.currency}"
                    # http://127.0.0.1:8000/graphics-cards/fr/nvidia-geforce-rtx-3080-12-gb-vs-nvidia-geforce-rtx-4090/
        return instances


    @property
    def gpu_image_name(self):
        return f"/static/assets/img/gpu_images/{format(self.name.lower().replace(' ', '-'))}.png"
    
    @property
    def brand_image(self):
        images = {
            'nvidia': "/static/assets/img/navidia.png",
            'amd': "/static/assets/img/amd.png",
            'ati': "/static/assets/img/ati.png",
            "intel": "/static/assets/img/intel.png",
        }
        key = 'nvidia'
        if 'nvidia' in self.name.lower():
            key = 'nvidia'
        elif 'amd' in self.name.lower():
            key = 'amd'
        elif 'ati' in self.name.lower():
            key = 'ati'
        elif 'intel' in self.name.lower():
            key = 'intel'
        return images[key]
    

    # @property
    # def compare_gpu(self):

