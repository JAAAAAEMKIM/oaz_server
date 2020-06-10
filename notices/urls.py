from django.urls import path
from notices import views

urlpatterns = [
    path('', views.NoticeListView.as_view()),
    path('<int:pk>/', views.NoticeUpdateView.as_view()),
]