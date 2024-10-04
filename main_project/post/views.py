from django.shortcuts import render, redirect
from .forms import PostCreateForm,CommentForm,UpdatePostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# from django.urls import reverse
# Create your views here.
from .models import Post
from django.contrib import messages

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('home')
    else:
        form = PostCreateForm()
        return render(request, 'post/create.html', {'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.liked_by.all():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('home')

def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    print(request.method)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.posted_by = request.user
            new_comment.save()
            messages.success(request, 'comment created successfully! Please log in.')
            return redirect('home')
    else:
        print('here')
        comment_form = CommentForm()
    posts = Post.objects.all()
    return render(request, 'Users/base2.html', {'posts': posts, 'logged_user': request.user, 'comment_form': comment_form})

def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        if 'delete' in request.POST:  # Check if the delete button was clicked
            post.delete()
            return redirect('home')
        else:
            form = UpdatePostForm(data=request.POST, files=request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home')  
    else:
        form = UpdatePostForm(instance=post)

    return render(request, 'post/update_post.html', {'form': form,'post':post})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if post.user == request.user:
        post.delete()
        messages.success(request, 'Post deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this post.')

    return redirect('profile')  # Change 'profile' to the appropriate redirect URL
