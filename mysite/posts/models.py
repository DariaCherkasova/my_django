from django.db import models
#from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

'''class Group(models.Model):
    title=models.TextField()
    description=models.CharField(max_length=200)'''

class Event(models.Model):
    name = models.CharField(max_length=200)
    start_at = models.DateTimeField()
    description = models.TextField()
    contact = models.EmailField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_author")
    location = models.CharField(max_length=400)

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="img/profile/")
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
def __str__(self):
    return str(self.user)