from django.urls import path
from .views import RegisterView, TestAPI

urlpatterns = [
    path('', TestAPI.as_view(), name='test-API'),
    
    path('register/', RegisterView.as_view(), name='register'),

    #
    # path('login/', LoginAPI.as_view(), name='loginAPI'), #Custom implementation of api-token-auth

    # path('change-password/', ChangePassword.as_view(), name='change-password-API')
]
