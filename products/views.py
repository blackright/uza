from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Products
from .forms import ProductForm


# Create your views here.

def home(request):
	#context = {
	#	'categories' 	:	Category.objects.all(),
	#}
	return render(request,'products/home.html')

def checkout(request, pk):
	context = {
		'products' 	:	Products.objects.filter(pk=pk),
	}
	return render(request,'products/checkout.html', context)

def about(request):
	#context = {
	#	'categories' 	:	Category.objects.all(),
	#}
	return render(request,'products/about.html')

class ProductListView(LoginRequiredMixin, ListView):
	model = Products
	template_name = 'products/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'products'
	ordering = ['created_date']
	paginate_by = 20

class ProductDetailView(LoginRequiredMixin, DetailView):
	model = Products

class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Products
	form_class = ProductForm
		



