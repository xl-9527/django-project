import os
import sys
import logging

logger = logging.getLogger('django')

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-project.settings.dev')
    try:
        from django.core.management import execute_from_command_line
        logger.info('Starting development server...')
    except Exception as e:
        logger.error(e)
    execute_from_command_line(sys.argv)