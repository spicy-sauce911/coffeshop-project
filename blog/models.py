from django.db import models

# Create your models here.
class Post(models.Model):
	post_title = models.CharField(max_length=300)
	post_time = models.DateTimeField(auto_now=True)
	post_image = models.ImageField(upload_to='event_images/')
	post_text = models.TextField(max_length=300)
