from django.shortcuts import render
from blog.models import BlogPost
from operator import attrgetter
# Create your views here.

def home_screen_view(request):
    context = {}

    query = ''
    if request.GET['q']:
        query = request.GET['q']
        context['query'] = str(query)

    blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'),reverse=True)
    context['blog_posts'] = blog_posts
    return render(request, 'snippets/home.html', context)