from django.shortcuts import render,get_object_or_404
from .models import blog

# Create your views here.
def all_blogs(requests):
    blogs=blog.objects.all()
    return render(requests,'blog/all_blogs.html',{'blogs':blogs})

def detail(requests,blog_id):
    det_blog=get_object_or_404(blog,pk=blog_id)

    return render(requests,'blog/detailed.html',{'blog':det_blog})
