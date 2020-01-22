from django.urls import path
from . import views as post_views

app_name = 'posts'

urlpatterns = [
    path('<id>/<slug>', post_views.post_detail, name="post_detail"),
    path('add_comment', post_views.add_comment, name='add_comment'),
    path('delete_comment', post_views.delete_comment, name='delete_comment')
]
