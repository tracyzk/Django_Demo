from django.shortcuts import render, render_to_response,HttpResponseRedirect
from article.models import Article
import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def add(request):
	if request.method == 'POST':
		title = request.POST.get('title', '')	
		author = request.POST.get('author', '')
		description = request.POST.get('description', '')
		content = request.POST.get('content', '')
		new = Article(title=title, author=author, description=description, content=content)		
		new.save()
		return HttpResponseRedirect('/manage')
	return render_to_response('article.add.html')

def manage(request):
	articles = Article.objects.order_by("-id").all()
	return render_to_response('article.manage.html', {'articles':articles})
	
def delete(request,id):
	Article.objects.filter(id=id).delete()
	return HttpResponseRedirect('/manage')

def modify(request, id):
	article = Article.objects.get(id=id)
	return render_to_response('article.modify.html', {'article': article})


@csrf_exempt
def modify_handle(request):
	if request.method == 'POST':
		id = request.POST.get('id', '')

		article = Article.objects.get(id = id)
		title = request.POST.get('title', '')	
		author = request.POST.get('author', '')
		description = request.POST.get('description', '')
		content = request.POST.get('content', '')

		article.title = title;
		article.author = author;
		article.description = description;
		article.content = content;
		article.save()
		return HttpResponseRedirect('/manage')
	return render_to_response('article.add.html')
	
