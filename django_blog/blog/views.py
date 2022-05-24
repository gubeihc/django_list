from django.shortcuts import render

from django.http import  HttpResponse
# Create your views here.
from blog.models import  Acticle
from django.core.paginator import Paginator

#定义视图函数

def hello_world(request):
    return HttpResponse("Hello World")
    # return render(request, 'heallo.html', {'hello': 'Hello World!'})


def article_content(request):
    article = Acticle.objects.all()[0]
    title = article.acticle_title
    brief_content = article.acticle_brief
    content = article.acticle_html
    article_id = article.acticle_id
    publish_data = article.acticle_publish_data

    return  HttpResponse("title:%s,brief_content:%s,content:%s,article_id:%s,publish_data:%s"%(title,brief_content,content,article_id,publish_data))
    # return render(request, 'article.html', locals())




def get_index_page(request):
    # 查询数据库，获取所有的文章
    page = request.GET.get('page')
    if page:
        page=int(page)
    else:
        page=1

    all_article = Acticle.objects.all()

    top_5_article_list = Acticle.objects.order_by("-acticle_publish_data")[:5]

    pagintator=Paginator(all_article,1)
    page_article_list=pagintator.page(page)

    if page_article_list.has_next():
        next_page=page+1
    else:
        next_page=page
    if page_article_list.has_previous():
        previous_page=page-1
    else:
        previous_page=page

    return render(request, 'blog/index.html', {'article_list': page_article_list,"page_num":range(1,pagintator.num_pages+1),
                                               "cirr_page":page,
                                               "next_page":next_page,
                                               "previous":previous_page,
                                               "top5_article_list":top_5_article_list,
                                               })


def get_detail_page(request,article_id):
    all_article = Acticle.objects.all()
    curr_article =None

    Previous=None
    Next_page=None
    for index,artc in enumerate(all_article):
        if index==0:
            Previous_index=0
            page_index=index +1
        elif index==len(all_article)-1:
            Previous_index=index-1
            page_index=index
        else:
            Previous_index=index-1
            page_index=index +1
        if artc.acticle_id == article_id:
            curr_article = artc
            Previous = all_article[Previous_index]
            Next_page = all_article[page_index]
            break


    section_list=curr_article.acticle_html.split('\n')

    return render(request, 'blog/detail.html', {'article_list': curr_article,"section_list":section_list,
                                                "Previous":Previous,
                                                "Next_page":Next_page,
                                                })


