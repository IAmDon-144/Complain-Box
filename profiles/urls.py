from django.urls import path, include
from .views import myProfile,editMyProfile,getProfile


urlpatterns = [


    path('my-profile/', myProfile, name='my-profile'),
    path('<pk>/<str:type>/profiles/', getProfile, name='get-profile'),
    path('edit-profile/<pk>/edit/', editMyProfile, name='edit-profile'),





]
