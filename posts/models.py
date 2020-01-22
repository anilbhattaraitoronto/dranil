from django.db import models


class Post(models.Model):
    TOPIC_CHOICES = (
        ('air', 'Air'),
        ('water', 'Water'),
        ('food', 'Food'),
        ('housing', 'Housing'),
        ('health', 'Health'),
        ('education', 'Education'),
        ('transportation', 'Transportation'),
        ('sexuality', 'Sexuality')
    )
    is_archived = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=80)
    keywords = models.CharField(max_length=250)
    summary = models.CharField(max_length=250)
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to='posts/images/%Y/%M')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_on', 'author', 'topic')

    def __str__(self):
        return self.title


class Comment(models.Model):
    # authenticated users can comment on posts
    #writer = request.user.get_full_name()
    #email = request.user.email
    writer = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ('posted_on', 'post', 'writer')

    def __str__(self):
        return self.writer


# Create your models here.
