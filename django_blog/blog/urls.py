from django.urls import path,include


from .views import *

urlpatterns = [

    path('hello_world',hello_world,name='hello'),
    path('content',article_content,name='article'),
    path('index',get_index_page,name='index_page'),
    # path('detail',get_detail_page,name='getdetail_page'),
    path('detail/<int:article_id>',get_detail_page,name='getdetail_page'),
]