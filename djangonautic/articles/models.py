from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE ,default=None)

    def __str__(self):
        return self.title

    def snippets(self):
        return self.body[:50] + '... see more'

    def upper(self):
        return self.title.upper()

    def editedAuthor(self):
        return '-- ' + str(self.author).capitalize()