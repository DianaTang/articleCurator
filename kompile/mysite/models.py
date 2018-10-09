# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Category (models.Model):
    category_text = models.CharField(max_length=100)

    def __str__(self):
        return self.category_text

class Article (models.Model):
    article_path = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    def __str__(self):
        return self.article_path

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
