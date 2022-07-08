from django.db import models

# Create your models here.
class BlogPost(models.Model):
    
    CATEGORY =(('science', '科学のこと'),
               ('dailylife', '日常のこと'),
               ('music', '音楽のこと'))
    
    #タイトル用のフィールド（column）
    title = models.CharField(
        verbose_name ='タイトル',
        max_length= 200
        )
    
    #本文中のフィールド
    content = models.TextField(
        verbose_name='本文'
        )
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name = '投稿日時',
        auto_now_add = True #日時を自動追加
        )
    #カテゴリのフィールド
    category = models.CharField(
        verbose_name='カテゴリ',
        max_length = 50,
        choices = CATEGORY
        )
    
    def __str__(self):
        return self.title
    
    
    
    