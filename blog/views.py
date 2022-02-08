from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from blog.forms import NewPostForm
from blog.models import Post


# Create your views here.
def home(request):
    return render(request, 'blog/base.html')


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'blog/post_list.html', context)


@login_required
def create_post(request):
    form = NewPostForm()
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)
