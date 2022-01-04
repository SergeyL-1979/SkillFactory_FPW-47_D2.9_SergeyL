from django.urls import path
from .views import NewsList, NewsDetail, CategoryPost

urlpatterns = [
    path('post/', NewsList.as_view(), name='post_list'),
    path('post-detail/<str:slug>/', NewsDetail.as_view(), name='post_detail'),
    path('category/<int:pk>/', CategoryPost.as_view(), name='category_detail'),
]
