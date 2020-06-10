from django.urls import path
from qnas import views

urlpatterns = [
    path('', views.QnaListCreateView.as_view()),
    path('<int:pk>/', views.QnaUpdateDestroyView.as_view()),
    path('get/<int:pk>/', views.QnaRetrieveView.as_view()),
    path('like/', views.LikeQnaView.as_view()),
    path('unlike/<int:pk>/', views.UnlikeQnaView.as_view()),
    path('comments/', views.QnaCommentCreateView.as_view()),
    path('comments/<int:pk>/', views.QnaCommentUpdateDestroyView.as_view()),
    path('comments/like/', views.LikeCommentView.as_view()),
    path('comments/unlike/<int:pk>/', views.UnlikeCommentView.as_view()),
    # path('comments/<int:pk>/', views.CommentRetrieveView.as_view()),
]