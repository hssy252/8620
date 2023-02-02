from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
User = get_user_model()

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null='True')
    id_user = models.IntegerField(null='True')
    img = models.ImageField(upload_to='client_images', default='铁子.png')
    location = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.user.username



class Post(models.Model):
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    title = models.TextField()
    passage = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    owner_id = models.ForeignKey(to='Client', on_delete=models.CASCADE, null='True')
    def __str__(self):
        return self.title
