from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'payment'
urlpatterns = [
	path('payment/<int:pk>/', views.payment_home, name='payment'),
]