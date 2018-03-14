from django.urls import path, include

urlpatterns = [
    path('', include('timestamp_app.urls')),
]
