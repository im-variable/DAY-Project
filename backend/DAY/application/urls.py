from django.urls import path
from .views import ListCreateAPIView, PostDetailAPIView


urlpatterns = [
    path('', ListCreateAPIView.as_view(), name='app-create'),
    path('<int:id>', PostDetailAPIView.as_view(), name='app-update'),
    
]
