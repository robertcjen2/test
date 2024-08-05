"""from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")"""

from django.http import HttpResponse
from django.template import loader
from members.models import Post
from django.template import Context, loader

def members(request):
  post_list = Post.objects.all().values()
  template = loader.get_template('myfirst.html')
  c = {'post_list': post_list,}
  return HttpResponse(template.render(c))

def details(request, id):
  mymember = Post.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
