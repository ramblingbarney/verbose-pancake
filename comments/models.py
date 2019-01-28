from django.db import models
from products.models import Product
from tinymce import HTMLField


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_wiki = HTMLField('Content')

    def __str__(self):
        return self.comment_id
