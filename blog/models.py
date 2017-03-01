from django.db import models
from django.contrib.auth.models import User

SHORT_TEXT_LEN = 150
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField(blank=False,auto_now=1, auto_now_add=0)
    image = models.ImageField(default= False, height_field=None, width_field= None)
    likes = models.IntegerField(blank=True, default=0)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text

class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comment = models.TextField(max_length=100, blank=False,)
    comment_time = models.DateTimeField(blank=False, auto_now=1, auto_now_add=0)
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE)