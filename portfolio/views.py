from django.shortcuts import render, redirect
from posts.models import Post, Comment
from posts.forms import PostCreateForm


def home_view(request):

    latest_posts = Post.objects.all()[:5]
    featured_post = Post.objects.filter(is_featured=True).first()
    comment_count = None
    if featured_post != None:
        comment_count = Comment.objects.filter(
            post_id=featured_post.id).count()

    context = {
        'latest_posts': latest_posts,
        'featured_post': featured_post,
        'comment_count': comment_count,
    }
    return render(request, 'index.html', context)
