from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from blog.forms import NewPostForm
from blog.models import Post


# Create your views here.
def post_list(request):
    # posts = Post.objects.all()
    # context = {
    #     "posts": posts
    # }
    return render(request, 'blog/post_list.html')


@login_required
def create_post(request):
    form = NewPostForm()
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)
