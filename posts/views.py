from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostCreateForm


def topic_posts(request, topic):
    topic_posts = Post.objects.filter(topic=topic)

    context = {
        'topic_posts': topic_posts,
        'topic': topic
    }
    return render(request, 'posts/topic_posts.html', context)


def post_detail(request, slug, id):
    post = get_object_or_404(Post, slug=slug, id=id)
    form = PostCreateForm(instance=post)
    comments = Comment.objects.filter(post_id=id)
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'posts/post_detail.html', context)


def create_post(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            form = PostCreateForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('posts:post_detail', post.id, post.slug)
            else:
                return redirect('home_view')
        else:
            return redirect('home_view')
    else:
        return redirect('home_view')


def update_post(request, id, slug):
    if request.user.is_authenticated and request.user.is_staff:

        if request.method == 'POST':
            post = get_object_or_404(Post, id=id, slug=slug)
            form = PostCreateForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('posts:post_detail', post.id, post.slug)
            else:
                return redirect('home_view')
        else:
            return redirect('home_view')

    else:
        return redirect('home_view')


def delete_post(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            post_id = request.POST['post_id']
            post = get_object_or_404(Post, id=post_id)
            post.delete()
            return redirect('home_view')
        else:
            return redirect('home_view')

    else:
        return redirect('home_view')


def add_comment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            writer = user.get_full_name()
            email = user.email
            post_id = request.POST.get('post_id', None)
            post = get_object_or_404(Post, id=post_id)
            slug = post.slug
            text = request.POST['text']
            comment = Comment(
                writer=writer, email=email, post=post, text=text)
            comment.save()
            return redirect('posts:post_detail', post_id, slug)
        else:
            return redirect('home_view')
    else:
        return redirect('home_view')


def delete_comment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_id = request.POST['comment_id']
            comment = get_object_or_404(Comment, id=comment_id)
            post = comment.post
            comment.delete()
            return redirect('posts:post_detail', post.id, post.slug)
        else:
            pass
    else:
        return redirect('posts:post_detail', post.id, post.slug)
