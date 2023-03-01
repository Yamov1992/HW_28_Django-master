
from django.urls import path

from ads import views

urlpatterns = [
    path('', views.AdsListView.as_view(), name = 'ad_list'),
    path('create/', views.AdsCreateView.as_view(), name='ads_create'),
    path('<int:pk>/', views.AdsDetailView.as_view(), name='ads_detail'),
    path('<int:pk>/upload_image/', views.AdsUploadImageView.as_view(), name='ads_upload_image'),
    path('<int:pk>/update/', views.AdsUpdateView.as_view(), name='ads_update'),
    path('<int:pk>/delete/', views.AdsDeleteView.as_view(), name='ads_delete'),
]