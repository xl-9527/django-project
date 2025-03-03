import logging

from django.shortcuts import render
from django.views import View
from models import DjangoUser

log = logging.getLogger('django')


# Create your views here.
class RegistryView(View):
    """用户注册"""

    def get(self, request):
        """访问用户祖册的页面"""
        return render(request, 'users/registry.html')

    def post(self, request):
        """处理用户注册的请求"""
        # log.info(request)
        post = request.POST
        log.info("用户名：" + post.get('username'))
        log.info('密码：' + post.get('password'))

        # DjangoUser(username=post.get('username'), password=post.get('password')).save()

        return render(request, 'index.html')
