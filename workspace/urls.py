from django.urls import path

from workspace.views import Main, Authorization, Registration, CreateResume

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('authorization/', Authorization.as_view(), name='authorization'),
    path('registration/', Registration.as_view(), name='registration'),
    path('create_resume/', CreateResume.as_view(), name='create-resume'),
]