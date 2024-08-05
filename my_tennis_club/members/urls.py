from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]

"""from django.template import Context, loader
from members.models import Post
from django.http import HttpResponse
def index(request):
	post_list = Post.objects.all()
	t = loader.get_template('members/index.html')
	c = Context({'post_list' : poll_list,})
	return HttpResponse(t.render(c))"""