from django.shortcuts import render
from django.views import generic
from store.models import Product
from django.db.models import Q
# Create your views here.

class ProductSearch(generic.ListView):
    model = Product
    template_name = 'index.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return Product.objects.all()
