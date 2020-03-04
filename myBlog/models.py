from django.db import models
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils import timezone, datetime_safe
import datetime
import os
from django.contrib.sitemaps import ping_google

# Create your models here.

# Create your models here.
class BigCategory(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_latest_post(self):
        result = Post.objects.filter(
            category__parent=self).filter(
            is_publick=True).order_by('-created_at')[:5]
        return result


class SmallCategory(models.Model):
    """ 小カテゴリー """
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(BigCategory, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_latest_post(self):
        result = Post.objects.filter(
            category=self).filter(
            is_publick=True).order_by('-created_at')[:5]
        return result


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="author")
    title = models.CharField("タイトル",max_length=200)
    thumbnail = models.ImageField(upload_to= 'media',verbose_name='サムネイル', default="A28WZDTYEY.jpg")
    text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')
    card_text = MarkdownxField('記事説明文', null=True,  help_text='Markdown形式で書いてください。')
    category = models.ForeignKey(SmallCategory, on_delete=models.PROTECT,  null=True, blank=True, related_name= "Category")
    is_public = models.BooleanField('公開可能か', default=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True,null=True)
    live = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            pass

    def text_to_markdown(self):
        return markdownify(self.text)

    def text_card_markdown(self):
        return markdownify(self.card_text)




