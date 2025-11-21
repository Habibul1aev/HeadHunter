from django.urls import path

from api.auth.views import LoginApiView, RegistrationApiView

urlpatterns = [
    path('login/', LoginApiView.as_view()),
    path('reqistration/', RegistrationApiView.as_view())
]