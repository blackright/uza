from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Products(models.Model):
	user 				=	models.ForeignKey(User, on_delete=models.CASCADE)
	name                =   models.TextField()
	description 		=	models.TextField()
	code 				=	models.TextField()
	price 				= 	models.IntegerField()
	image 				=	models.ImageField(default='default.jpeg', upload_to='products_pics')
	status              =   models.CharField(max_length=200)
	created_date		=	models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

	#def get_absolute_url(self):
		#return reverse('products:product-detail', kwargs={'pk': self.pk}) 
		#this will take us to the post detail for the specific question we have just added
