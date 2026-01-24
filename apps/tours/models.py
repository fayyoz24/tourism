from django.db import models
from .functions import guide_image_dir
from users.models import User
# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Language"          # singular name
        verbose_name_plural = "Languages"  # plural name

class Guide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    las_name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(default=f"Hello My name is {user.username}")
    profile_picture = models.ImageField(upload_to=guide_image_dir)
    lang = models.ManyToManyField(Language, related_name='guides')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class GuidePost(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]

class GuidePostImage(models.Model):
    post = models.ForeignKey(GuidePost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='guide_posts/')

    def __str__(self):
        return f"Image for: {self.post.guide}- {self.post.title}"

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='tours')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
