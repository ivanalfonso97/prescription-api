from django.urls import path 

from . import views

urlpatterns = [
  path('', views.prescription_list_create_view),
  path('<int:pk>/', views.prescription_detail_view),
  path('<int:pk>/update/', views.prescription_update_view),
  path('<int:pk>/delete/', views.prescription_destroy_view),
]