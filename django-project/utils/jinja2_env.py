from jinja2 import Environment
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage

def jinja2_env(**options):
    env = Environment(**options)

    # 自定义 jinja2 的语法
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse
    })

    return env