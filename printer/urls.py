from django.urls import path
from .views import index

app_name = 'printer'

urlpatterns = [
  path('', index, name='index')
]