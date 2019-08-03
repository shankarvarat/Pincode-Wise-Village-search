from django.urls import path
from .views import *
urlpatterns = [
    path('', search_status),
    path('search_status', search_status,name='index'),
    path('search', search),

]
