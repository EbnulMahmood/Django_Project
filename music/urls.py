from django.urls import path
from .views import AudioListView, AudioDetailView, updoad_audio, AudioUpdateView, AudioDeleteView


urlpatterns = [
    path('music/', AudioListView.as_view(), name='music-home'),
    path('music/<int:pk>/', AudioDetailView.as_view(), name='music-detail'),
    path('music/upload/', updoad_audio, name='music-upload'),
    path('music/<int:pk>/update/', AudioUpdateView.as_view(), name='music-update'),
    path('music/<int:pk>/delete/', AudioDeleteView.as_view(), name='music-delete'),
]