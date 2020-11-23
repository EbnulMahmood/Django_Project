from django.urls import path
from .views import VideoListView, VideoDetailView, updoad_video, VideoUpdateView, VideoDeleteView


urlpatterns = [
    path('video/', VideoListView.as_view(), name='video-home'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('video/upload/', updoad_video, name='video-upload'),
    path('video/<int:pk>/update/', VideoUpdateView.as_view(), name='video-update'),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name='video-delete'),
]