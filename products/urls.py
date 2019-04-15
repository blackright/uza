from django.urls import path
from django.conf.urls import url
from .views import (
	ProductListView,
	ProductDetailView,
	ProductCreateView,
)
from . import views

app_name = 'products'
urlpatterns = [
	path('',ProductListView.as_view(), name='products-home'),
	path('product/new/',ProductCreateView.as_view(), name='products-create'),
	path('product/<int:pk>/',ProductDetailView.as_view(), name='products-detail'),
	path('product/<int:pk>/checkout/',views.checkout, name='products-checkout'),
	path('about/', views.about, name='products-about'),
]