from django import forms

from .models import Video


class VideoForm(forms.ModelForm):
    """Форма для видео."""

    class Meta:
        model = Video
        fields = '__all__'
