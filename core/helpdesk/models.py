from django.db import models
import datetime
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_models


class Article(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    body = tinymce_models.HTMLField()
    pub_time = models.DateTimeField("date published", default=timezone.now())
    pub_update_time = models.DateTimeField("date updated", default=timezone.now())
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    cat = TreeForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='articles')
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_time >= timezone.now() - datetime.timedelta(days=1)


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=150)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = [['parent', 'slug']]

    def __str__(self):
        return self.name
