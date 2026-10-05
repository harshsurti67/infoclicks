from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def api_root(request):
    return JsonResponse({
        "name": "InfoClicks Backend API",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": {
            "contact": "/api/contact/",
            "admin": "/admin/"
        }
    })


urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('contact.urls')),
]
