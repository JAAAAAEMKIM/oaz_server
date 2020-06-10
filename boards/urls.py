from django.urls import path
from boards import views

urlpatterns = [
    path('', views.PostListCreateView.as_view()),
    path('<int:pk>/', views.PostUpdateDestroyView.as_view()),
    path('get/<int:pk>/', views.PostRetrieveView.as_view()),
    path('like/', views.LikePostView.as_view()),
    path('unlike/<int:pk>/', views.UnlikePostView.as_view()),
    path('comments/', views.CommentCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentUpdateDestroyView.as_view()),
    path('comments/like/', views.LikeCommentView.as_view()),
    path('comments/unlike/<int:pk>/', views.UnlikeCommentView.as_view()),
    # path('comments/<int:pk>/', views.CommentRetrieveView.as_view()),
]