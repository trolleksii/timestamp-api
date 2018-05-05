from django.urls import path

from timestamp_project.settings import SITE_URL

from .views import IndexView, TimeStampView

app_name = 'timestamp_app'

urlpatterns = [
    path('', IndexView.as_view(), {'site_url': SITE_URL}, name='index_view'),
    path('<str:date>/', TimeStampView.as_view(), name='timestamp_view'),
]
