from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
app_name = 'blog'

urlpatterns = [
    path('create/',views.create_blog_view, name='create'),
    path('<slug>/',views.detail_blog_view, name='detail'),
    path('<slug>/edit',views.edit_blog_view, name='edit'),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)