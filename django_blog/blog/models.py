from django.db import models

# Create your models here.

class Acticle(models.Model):
    """
    文章唯一id
    文章标题
    文章摘要
    文章发布日期

    """
    acticle_id=models.AutoField(primary_key=True)
    acticle_title=models.TextField(max_length=100)
    acticle_brief=models.TextField(max_length=200)
    acticle_html=models.TextField()
    #发布日子 自动默认当前创建日期
    acticle_publish_data =models.DateTimeField(auto_now_add=True)



    def __str__(self):
        #这里返回文章title
        return self.acticle_title

