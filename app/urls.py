from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('subjects/', views.SubjectListCreateView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', views.SubjectDetailView.as_view(), name='subject-detail'),
    path('marks/', views.MarkListCreateView.as_view(), name='mark-list'),
    path('marks/<int:pk>/', views.MarkDetailView.as_view(), name='mark-detail'),
]
