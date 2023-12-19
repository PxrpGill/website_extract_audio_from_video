from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import DetailView
import os

import moviepy.editor as mp

from .forms import VideoForm
from .models import User


def upload_video(request):
    # Алгоритм преобразования
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)

        if form.is_valid():
            video = form.save()
            video_path = video.video_file.path
            audio_path = video_path.replace('.mp4', '.mp3')
            clip = mp.VideoFileClip(video_path)
            clip.audio.write_audiofile(audio_path, codec='mp3')
            os.rename(
                audio_path,
                f'T:\\tests_pyhton\\website_extract_audio_from_video\\website\\media\\videos\\{video.title}.mp3'
            )
            if os.path.exists(audio_path):
                os.remove(audio_path)
            audio_path = f'T:\\tests_pyhton\\website_extract_audio_from_video\\website\\media\\videos\\{video.title}.mp3'
            context = {
                'audio_path': audio_path,
            }
            return render(
                request,
                'converter/success.html',
                context
            )
    else:
        form = VideoForm()
        return render(
            request,
            'converter/upload_video.html',
            {'form': form}
        )


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """Детальное отображение пользователя."""

    model = User
    slug_url_kwarg = 'username'
    slug_field = 'username'
    context_object_name = 'profile'
    template_name = 'converter/profile.html'


def download_audio(request, file_path):
    # Отправка файла пользователю для загрузки
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response
