from .models import Post
from .forms import PostCreateForm


def post_titles(request):
    topics = Post.TOPIC_CHOICES
    post_titles = Post.objects.values('title', 'id', 'slug')
    context = {
        'topics': topics,
        'post_titles': post_titles,
        'create_post_form': PostCreateForm
    }
    return context
