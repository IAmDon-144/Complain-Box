from django.urls import path, include
from .views import getAllComplain, getSingleComplain, addComplain,editPost,deletePost,commentPost,deleteComment,likeSame,changeStatus


urlpatterns = [


    path('', getAllComplain, name='home'),
    path('add/', addComplain, name='add-complain'),
    path('<pk>/<str:title>/details/', getSingleComplain, name='post-details'),
    path('<pk>/<str:title>/edit/', editPost, name='edit-post'),
    path('<pk>/<str:title>/delete/', deletePost, name='post-delete'),
    path('<pk>/comment/', commentPost, name='comment-post'),
    path('<pk>/<str:type>/<ck>/dc/', deleteComment, name='delete-comment'),
    path('like-same/', likeSame, name='like-same'),
    path('<pk>/<str:type>/<ck>/edit-status/', changeStatus, name='status-edit'),



]
