from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = 'youtube'

urlpatterns = [
    path('addVideo/', views.AddVideo.as_view(), name='addVideo'),
    path('video/<int:pk>/', views.PlayVideo.as_view(), name='playVideo'),
    path('video/video_list/', views.VideoList.as_view(), name='videoList'),
    path('video/<int:pk>/update/', views.UpdateVideo.as_view(), name='update'),
    path('video/<int:pk>/delete/', views.DeleteVideo.as_view(), name='delete'),
    path('video_str/<str:title>/', views.seeVideo, name='seeVideo'),
    path('addChannel/', views.addChannel.as_view(), name='addChannel'),
    path('channel/<int:pk>/', views.SomeoneChannel.as_view(), name='someoneChannel'),
    path('channel/myChannel/', views.MyChannel, name='channel'),
    path('channel/<int:pk>/update/', views.UpdateChannel.as_view(), name='update_channel'),
    path('channel/<int:pk>/delete/', views.DeleteChannel.as_view(), name='delete_channel'),
]