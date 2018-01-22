from django.db import models
from datetime import datetime
# Create your models here.

class Upload(models.Model):
	DownloadDocount = models.IntegerField(verbose_name=u'访问次数',default=0)
	code = models.CharField(max_length=8,verbose_name=u'code')
	Datetime =models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
	path = models.CharField(max_length=32,verbose_name=u'下载路径')
	name = models.CharField(max_length=32,verbose_name=u'文件名',default='')
	Filesize = models.CharField(max_length=32,verbose_name=u'文件大小')
	PCIP = models.CharField(max_length=32,verbose_name=u'IP地址',default='')

	class Meata(): # Meta 可用于定义数据表名，排序方式等。
		verbose_name = 'download' #指明一个易于理解和表示的单词形式的对象
		db_table = 'download' #声明数据表的名db_table 定义数据表名,否则 Django 会给表名设置默认名称 appname_modelname
	def __str__(self): #表示在做查询操作时，我们看到的是 name 字段
		return self.name

			
		