from django.urls import path
from .views import signup_view, home_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home_view, name='home'),  # 홈 화면 URL
]
