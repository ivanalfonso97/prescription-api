from django.urls import path 

from . import views

urlpatterns = [
  path('', views.prescription_list_create_view, name='prescription-list'),
  path('<int:pk>/', views.prescription_detail_view, name='prescription-detail'),
  path('<int:pk>/update/', views.prescription_update_view, name='prescription-edit'),
  path('<int:pk>/delete/', views.prescription_destroy_view),
]