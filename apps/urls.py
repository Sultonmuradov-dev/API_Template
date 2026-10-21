from django.urls import path
from apps.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('posts/<int:pk>/update/', PostUpdateView.as_view()),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view()),
]