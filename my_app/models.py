from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200,null=False,blank=False)

	def __str__(self):
		return self.name



class Post(models.Model):
	category = models.ForeignKey(Category,blank=False,null=True,on_delete=models.SET_NULL)
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/')
	body = models.TextField()

	def __str__(self):
		return self.title


# Create your models here.
