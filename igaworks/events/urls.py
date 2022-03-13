from django.urls import path
from .views import CollectEventAPI

urlpatterns = [
    path('collect', CollectEventAPI.as_view()),
    # path('search', SearchEventAPI.as_view()),
]
