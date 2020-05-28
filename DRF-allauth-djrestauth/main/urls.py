from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # all-auth urls
    # path('accounts/', include('allauth.urls')),

    # dj-rest-auth urls
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls'))
]
