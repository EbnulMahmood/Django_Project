from django.urls import path
from .views import PDFListView, PDFDetailView, upload_book, PDFUpdateView, PDFDeleteView


urlpatterns = [
    path('audiobook/', PDFListView.as_view(), name='audiobook-home'),
    path('audiobook/<int:pk>/', PDFDetailView.as_view(), name='audiobook-detail'),
    path('audiobook/upload/', upload_book, name='audiobook-upload'),
    path('audiobook/<int:pk>/update/', PDFUpdateView.as_view(), name='audiobook-update'),
    path('audiobook/<int:pk>/delete/', PDFDeleteView.as_view(), name='audiobook-delete'),
]