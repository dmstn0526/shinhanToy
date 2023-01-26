from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


from .models import Order, Comment
from .serializers import OrderSerializer, CommentSerializer, CommentCreateSerializer
# from .paginations import ProductLargePagination

class OrderListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class OrderDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)

class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        if order_id:
            return Comment.objects.filter(order_id=order_id) \
                .select_related('member','order') \
                .order_by('-id')
        return Comment.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)



