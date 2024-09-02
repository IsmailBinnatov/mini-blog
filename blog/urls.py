from django.urls import path

from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.PostView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('reviews/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add_like/', views.AddLike.as_view(), name='like'),
    path('<int:pk>/del_like/', views.DisLike.as_view(), name='dislike'),
]
