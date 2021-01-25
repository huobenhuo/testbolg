from django.db import models

# Create your models here.

class Article(models.Model):
    # 唯一ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章主要内容
    content = models.TextField()
    # 发布日期
    publish_date = models.DateTimeField(auto_now=True)

    content_a = models.CharField(max_length=10, default='1')

    def __str__(self):
        return self.title
