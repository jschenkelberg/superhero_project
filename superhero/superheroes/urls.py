from django.urls import path
from . import views
from .models import Superhero
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

# from django.conf.urls.static import staticfiles_urlpatterns

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:superhero_id>', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('edit/<int:superhero_id>', views.edit, name='edit'),
    path('delete/<int:superhero_id>', views.delete, name='delete'),
    path('static/batman.jpg', views.index)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
