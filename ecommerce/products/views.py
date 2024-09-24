from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# View para listar todos os produtos e criar novos
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# View para acessar, editar e deletar um produto específico
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer