from django.urls import path
from . import views

app_name = 'gps'

urlpatterns = [
    path('', views.TopPage.as_view(), name='top_page'),
]
