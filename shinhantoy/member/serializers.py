from rest_framework import serializers
from django.contrib.auth.hashers import make_password #암호화

from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Too short password')
            # 비밀번호가 8자보다 짧으면 validationError 발생
        return make_password(value)

    class Meta:
        model = Member
        fields = ('id','username','tel','password')
        extra_kwargs = {
            'id' : {
                'read_only': True,
            },
            'password':{
                'write_only': True
            }
        }
