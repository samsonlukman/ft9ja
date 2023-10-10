from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("dashb.urls")),  # Corrected URL pattern
    path('admin/', admin.site.urls),
]
