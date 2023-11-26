from django.urls import path
from .views import HomeView, loginView, register

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/login/', loginView.as_view(), name='login'),
    # path('register/', registerView.as_view(), name='register'),
    path('register/', register, name='register'),
]
