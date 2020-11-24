from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('post-list/', views.post_list),
    path('post-detail/<str:pk>/', views.post_detail),
    path('post-create/', views.post_create),
    path('post-update/<str:pk>/', views.post_update),
    path('post-delete/<str:pk>/', views.post_delete),
]
