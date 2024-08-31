from django.urls import path

from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.PostView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]
