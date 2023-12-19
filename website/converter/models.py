from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Video(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Придумайте название будущему файлу'
    )
    video_file = models.FileField(
        upload_to='videos/',
        verbose_name='Место загрузки файла',
        help_text=(
            'Выберите файл на вашем'
            ' компьютере для получения аудио'
        )
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'Видео'

