from django.contrib import admin
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.urls import path, include

from headhunter import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='admin-main'),
    path('cards/', views.cards, name='cards'),
    path('agreement/', views.agreement, name='agreement'),
    path('employer/', views.employer, name='employer'),
    path('help/', views.help, name='help'),
    path('workspace/', include('workspace.urls')),
    path('myresume', views.myResume, name='myresume'),
    path('api/v1/', include('api.urls')),
    # path('api/v1/', include('api.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)