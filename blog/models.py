from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): #定義object
    author = models.ForeignKey(User) #作者
    title = models.CharField(max_length=200) #標題
    text = models.TextField() #文章內容
    created_date = models.DateTimeField( #發文日期
            default=timezone.now)
    published_date = models.DateTimeField(  #發文日期
            blank=True, null=True)

    def publish(self): #publish 方法
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  #回傳網誌標題
        return self.title
