from django_filters import rest_framework as filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from guide.models import Product, ProductHistory, Category
from guide.serializers import ProductSerializer, ProductHistorySerializer, CategorySerializer


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    price = filters.RangeFilter()
    volume = filters.RangeFilter()
    alcohol = filters.RangeFilter()
    alcohol_price = filters.RangeFilter()
    category = filters.ModelMultipleChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ()


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all().filter()
    serializer_class = ProductSerializer
    filter_class = ProductFilter


class ProductHistoryViewSet(ReadOnlyModelViewSet):
    queryset = ProductHistory.objects.all()
    serializer_class = ProductHistorySerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
