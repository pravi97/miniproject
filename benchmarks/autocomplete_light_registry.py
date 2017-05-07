import autocomplete_light.shortcuts as al
from .models import Benchmark

class BenchmarkAutocomplete(al.AutocompleteModelBase):
    search_fields = ['number', 'name']

al.register(Benchmark, BenchmarkAutocomplete)
