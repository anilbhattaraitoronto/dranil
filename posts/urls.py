from django.urls import path
from . import views as post_views

app_name = 'posts'

urlpatterns = [
    path('topics/<topic>', post_views.topic_posts, name='topic_posts'),
    path('<id>/<slug>', post_views.post_detail, name='post_detail'),
    path('create_post', post_views.create_post, name='create_post'),
    path('<id>/<slug>/update_post', post_views.update_post, name='update_post'),
    path('delete_post', post_views.delete_post, name='delete_post'),
    path('add_comment', post_views.add_comment, name='add_comment'),
    path('delete_comment', post_views.delete_comment, name='delete_comment')
]
