from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('api.urls', namespace='accounts')),

    path('api/v1/', include('api.urls', namespace='apiaccounts')),
]
