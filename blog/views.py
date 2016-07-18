from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts1 = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'posts': posts1})