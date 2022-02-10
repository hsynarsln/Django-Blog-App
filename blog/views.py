
from email.policy import default
from multiprocessing import context

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render

from blog.forms import LikePost, NewPostForm, PostComment
from blog.models import Comment, Like, Post, PostView


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    likes = Like.objects.all()
    post_views = PostView.objects.all()
    context = {
        "posts": posts,
        "comments": comments,
        "likes": likes,
        "post_views": post_views,
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
        'form': form,
    }
    return render(request, 'blog/post_create.html', context)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    comments_count = comments.count()
    likes = Like.objects.filter(post=post)
    likes_count = likes.count()
    if request.user.is_authenticated:
        view = PostView()
        view.post = post
        view.user = request.user
        view.save()
    post_views = PostView.objects.filter(post=post)
    post_view_count = post_views.count()
    form = PostComment()
    form_like = LikePost()
    if request.method == "POST":
        form = PostComment(request.POST)
        form_like = LikePost(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully')
            return redirect('post_detail', id=id)
        elif form_like.is_valid():
            if request.user.is_authenticated:
                if likes.filter(user=request.user).exists():
                    pass
                else:
                    like = Like()
                    like.user = request.user
                    like.post = post
                    like.save()
                    messages.success(request, 'Post liked successfully')
                return redirect('post_detail', id=id)
            else:
                messages.error(request, 'Login required')
    context = {
        'post': post,
        'comment_form': form,
        "comments": comments,
        "comments_count": comments_count,
        "likes_count": likes_count,
        "like_form": form_like,
        'post_views': post_view_count,
    }
    return render(request, "blog/post_detail.html", context)


# def post_like(request, id):
#     post = Post.objects.get(id=id)
#     likes = Like.objects.filter(post=post)
#     form = LikePost()
#     if request.method == "POST":
#         form = LikePost(request.POST)
#         if request.user.is_authenticated:
#             if request.POST.get('liked') == 'True':
#                 if likes.filter(user=request.user).exists():
#                     pass
#                 else:
#                     like = Like()
#                     like.user = request.user
#                     like.post = post
#                     like.save()
#                     messages.success(request, 'Post liked successfully')
#             else:
#                 if likes.filter(user=request.user).exists():
#                     like = Like.objects.get(post=post, user=request.user)
#                     like.delete()
#                     messages.success(request, 'Post unliked successfully')
#                 else:
#                     pass
#     context = {
#         "like_form": form,
#     }
#     return render(request, "blog/post_detail.html", context)


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
