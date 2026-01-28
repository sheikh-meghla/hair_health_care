from django.urls import path

from apps.user.views import ChangePasswordAPIView, CustomUserAPIView, SignInAPIView, SignOutAPIView, SignUpAPIView

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('signout/', SignOutAPIView.as_view(), name='signout'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('user-info/', CustomUserAPIView.as_view(), name='user-info'),
]