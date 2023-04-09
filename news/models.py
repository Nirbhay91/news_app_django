from django.db import models

class News(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    source = models.URLField()

    def __str__(self):
        return self.name
