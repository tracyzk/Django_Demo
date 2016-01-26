from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from article.models import Article

# Create your views here.

def list(request):
	articles = Article.objects.order_by("-id").all()
	return render_to_response('article.list.html', {'articles':articles})

def show(request, id):
	article = Article.objects.get(id=id)
	return render_to_response('article.show.html',{'article':article})

def search(request):
	if 'key' in request.GET and request.GET['key']:
		key = request.GET['key']
		articles = Article.objects.filter(title__icontains=key)
		return render_to_response('article.list.html', {'articles':articles})
	else:
		return HttpResponse('Please submit a search term.')
