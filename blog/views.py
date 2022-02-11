from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'PeterL',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2022',
    },
    {
        'author': 'JerryL',
        'title': 'Blog post 2',
        'content': '2nd post content',
        'date_posted': 'August 29, 2022',
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts,
        'title': "Home Page",
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        
    }
    return render(request, 'blog/about.html', context)


