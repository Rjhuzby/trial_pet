from django.contrib import admin
from django.urls import path, include
from myapp.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # http://127.0.0.1:8000/
    path('myapp/', include('myapp.urls', namespace='myapp')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)