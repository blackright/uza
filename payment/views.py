from django.shortcuts import render

# Create your views here.
def payment_home(request, pk):
    	#context = {
	#	'categories' 	:	Category.objects.all(),
	#}
	return render(request,'payment/pay.html')