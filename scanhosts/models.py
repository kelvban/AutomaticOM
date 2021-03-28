# -*-coding:utf-8 -*-

from django.db import models

# Create your models here.

class UserIPInfo(models.Model):
	ip=models.CharField(max_length=40,default='',verbose_name=u'ip地址',null=True)
	time=models.DateTimeField(verbose_name=u'更新时间',auto_now=True)

	class Meta:
		verbose_name=u'用户访问地址信息表'
		verbose_name_plural=verbose_name
		db_table="user_ip_info"

class BrowseInfo(models.Model):
	user_agent=models.CharField(max_length=100,default='',verbose_name=u'用户浏览器agent信息',null=True)
	models.CharField(max_length=256,verbose_name=u'唯一设备ID',default="")

	user_ip=models.ForeignKey('UserIPInfo')

	class Meta:
		verbose_name=u'用户浏览信息表'
		verbose_name_plural=verbose_name
		db_table="browse_info"
