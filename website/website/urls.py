from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('converter:index'),
        ),
        name='registration',
    ),
    path('', include('converter.urls', namespace='converter')),
    path('pages/', include('pages.urls', namespace='pages')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
