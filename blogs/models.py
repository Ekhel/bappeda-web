from tokenize import blank_re
from django.db import models
from users.models import Profile

import uuid


class Article(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=False, unique=True)
    aricle_image = models.ImageField(
        upload_to='article_images/', null=True, blank=True, default='article_images/default.jpg')
    created_date = models.DateField(auto_now_add=True)
    id_article = models.UUIDField(default=uuid.uuid4, unique=True,
                                  primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)
