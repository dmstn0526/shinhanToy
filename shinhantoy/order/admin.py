from django.contrib import admin
from .models import Order, Comment

# Register your models here.
# 관리자 페이지에 나올려면 register 해줘야 한다.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass