from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): #定義object
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=200) #標題
    text = models.TextField() #文章內容
    photo = models.URLField(blank=True)
    created_date = models.DateTimeField( #發文日期
            default=timezone.now)

    def publish(self): #publish 方法
        self.create_date = timezone.now()
        self.save()

    def __str__(self):  #回傳網誌標題
        return self.title
