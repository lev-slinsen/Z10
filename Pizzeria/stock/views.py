from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def home(request):
    posts = Article.objects.all()
    return render(request, 'stock/home.html', {'posts': posts})
    # res = '<h1>Список пицц</h1>'
    # for post in posts:
    #     res += f'<div><h3>{post.name}</h3><div>{post.description}<hr>'
    # return HttpResponse(res)


def test(request):
    return HttpResponse('<h1>Test Page</h1>')
