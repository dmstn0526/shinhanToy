from rest_framework import serializers

from .models import Order, Comment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer): # 가져가기 위한 serializer
    # order_name = serializers.SerializerMethodField()
    member_username = serializers.SerializerMethodField() # data를 가져갈 때 data를 정의할 수 있는 field
    
    # method 필드는 함수.. 너가 만든 함수 안에서 필요하면 가져다 쓸게... 따라서 함수가 있어야 함 -> get_member_username
    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )
    
    def get_member_username(self,obj):
        return obj.member.username

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required = False
    )
    
    class Meta:
        model = Comment
        fields = '__all__'