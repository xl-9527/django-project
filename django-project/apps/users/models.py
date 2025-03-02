from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class DjangoUser(AbstractUser):
    """
    用户 django 等用户信息，因为需要加入一个手机号字段但是并没有，所以这里加入自定义的类，extends AbstractUser
    """
    phone = models.CharField(max_length=11, verbose_name="手机号", unique=True)

    class Meta:
        db_table = 'django_user' # custom table name
        verbose_name = 'django用户表' # comment
        verbose_name_plural = verbose_name