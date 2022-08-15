from django.shortcuts import render
from django.views.generic import DetailView,UpdateView,DeleteView,CreateView
from .models import Post,Category
from django.urls import reverse_lazy


def indexPage(request):
	posts = Post.objects.all()
	context = {
	"yangiliklar":posts,
	}
	return render(request,'index.html',context)


def footherPage(request,category_id):
	category = Category.objects.get(pk=category_id)
	posts = Post.objects.all().filter(category_id=category_id)
	context = {
	"category_name":category,
	"xabarlar":posts
	}
	return render(request,'foother.html',context)

def post_detailPage(request,nevs_id):
	pos = Post.objects.filter(id=nevs_id)
	dic = {
	"yangilik":pos[0]
	}
	return render(request,'post_detail.html',dic) 

# Create your views here.
