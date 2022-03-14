from django.urls import path
from .views import CollectEventAPI, SearchEventAPI

urlpatterns = [
    path('collect', CollectEventAPI.as_view()),
    path('search', SearchEventAPI.as_view()),
]
