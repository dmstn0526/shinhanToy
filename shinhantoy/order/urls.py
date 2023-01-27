from django.urls import path
from . import views

urlpatterns = [
    path("/<int:pk>", views.OrderDetailView.as_view()),
    # <>사이에 자료형이 나오고 뒤에 변수명을 씀.
    path("/<int:order_id>/comment", views.CommentListView.as_view()),
    # 변수는 가변인자(**kwargs)를 통해 들어온다.
    path("/comment", views.CommentCreateView.as_view()),
    path("/<int:order_id>/comment/<int:pk>", views.CommentDetailView.as_view()),
    path("", views.OrderListView.as_view()),
]