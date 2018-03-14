from django.urls import path

from .views import IndexView, TimeStampView

app_name = 'timestamp_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('<str:date>/', TimeStampView.as_view(), name='timestamp_view'),
]
