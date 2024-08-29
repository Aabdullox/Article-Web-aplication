from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=221)
    description = models.TextField()
    category = models.CharField(max_length=221)
    author_full_name = models.CharField(max_length=221)
    author_image = models.ImageField(upload_to='images_author/')
    author_job = models.CharField(max_length=221)
    image = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"