from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


from .models import Order
from .serializers import OrderSerializer
# from .paginations import ProductLargePagination

class OrderListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
