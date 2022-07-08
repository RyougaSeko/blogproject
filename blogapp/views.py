from django.shortcuts import render

#ListViewをインポート
from django.views.generic import ListView, DetailView

#モデルBlogPostをインポート
from .models import BlogPost

class IndexView(ListView):
    
    '''トップページのビュー
    

    
    
    
    '''
    
    
    #index.htmlをレンダリングする
    template_name = 'index.html'
        
    #object_listキーの別名を設定
    context_object_name = 'orderby_records'
    
    #BlogPostのレコードを投稿日時の降順で並び替える(データベースへの要求を行うためのオブジェクト)
    queryset = BlogPost.objects.order_by('-posted_at')
    

class BlogDetail(DetailView):
    '''
    詳細ページのview
    
    '''
    
    template_name = 'post.html'
    
    model = BlogPost
    
class ScienceView(ListView):
    template_name = 'science_list.html'
    
    model = BlogPost
    
    context_object_name = 'science_records'
    
    queryset = BlogPost.objects.filter(
        category='science').order_by('-posted_at')
    
        
class DailylifeView(ListView):
    template_name = 'dailylife_list.html'
    
    model = BlogPost
    
    context_object_name = 'dailylife_records'
    
    queryset = BlogPost.objects.filter(
        category='dailylife').order_by('-posted_at')
        
class MusicView(ListView):
    template_name = 'music_list.html'
    
    model = BlogPost
    
    context_object_name = 'music_records'
    
    queryset = BlogPost.objects.filter(
        category='music').order_by('-posted_at')
    
    