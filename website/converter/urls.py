from django.urls import path

from . import views


app_name = 'converter'

urlpatterns = [
    path('', views.upload_video, name='index'),
    path('profile/<username>/', views.ProfileDetailView.as_view(), name='profile'),
    path('download_file/<str:file_path>/', views.download_audio, name='download_file')
]
