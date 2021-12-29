from django.views.generic import ListView
from django.db.models import Q

from .models import Product


class ProductListView(ListView):
    paginate_by = 2
    model = Product
    template_name = 'home_page.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
        if category is not None:
            queryset = queryset.filter(category_id=category)
        return queryset
