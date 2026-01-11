from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Guide(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='guides/')
    lang = models.ManyToManyField(Language, related_name='guides')

    def __str__(self):
        return self.name

class GuidePost(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GuidePostImage(models.Model):
    post = models.ForeignKey(GuidePost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='guide_posts/')

    def __str__(self):
        return f"Image for {self.post.title}"

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='tours')

    def __str__(self):
        return self.title