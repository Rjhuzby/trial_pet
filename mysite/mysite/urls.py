from django.contrib import admin
from django.urls import path, include
from myapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # http://127.0.0.1:8000/
    path('myapp/', include('myapp.urls', namespace='myapp')),
]
