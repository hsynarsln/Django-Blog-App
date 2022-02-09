
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render

from blog.forms import NewPostForm, PostComment
from blog.models import Comment, Post


# Create your views here.
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
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post added successfully')
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    form = PostComment()
    if request.method == "POST":
        form = PostComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully')
            return redirect('post_detail', id=id)
    context = {
        'post': post,
        'comment_form': form,
        "comments": comments,
    }
    return render(request, "blog/post_detail.html", context)


# def send_comment(request):
#     form = PostComment()
#     if request.method == "POST":
#         form = PostComment(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = request.post
#             comment.user = request.user
#             comment.save()
#             messages.success(request, 'Comment added successfully')
#             return redirect('post_detail', id=id)
#     return render(request, 'blog/post_list.html')


def post_update(request, id):
    post = Post.objects.get(id=id)
    form = NewPostForm(instance=post)
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('post_detail', id=id)
    context = {
        'update_form': form,
    }
    return render(request, 'blog/post_update.html', context)


def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully')
        return redirect('home')
    context = {
        "post": post,
    }
    return render(request, 'blog/post_delete.html', context)
