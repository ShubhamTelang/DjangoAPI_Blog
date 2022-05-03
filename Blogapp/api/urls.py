from django.urls import path
from Blogapp.api.views import allpost,post
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('allpost/', allpost.as_view(),name='allpost'),
    path('post/<int:pk>', post.as_view(),name='post'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
