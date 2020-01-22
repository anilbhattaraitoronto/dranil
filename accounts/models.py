from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserMessage(models.Model):
    # get user name and user email from authenticated user
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=80)
    subject = models.CharField(max_length=250, blank=False)
    message = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('send_date', 'name')

    def __str__(self):
        return self.name
