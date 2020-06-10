from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('users/', include('rest_auth.urls')),  # url for users
    path('users/registration/', include('rest_auth.registration.urls')),
    path('users/user/', include('users.urls')),  # url for users
    path('boards/', include('boards.urls')),
    path('notices/', include('notices.urls')),
    path('qnas/', include('qnas.urls')),
]
