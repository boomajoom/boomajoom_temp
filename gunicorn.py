import os

bind = '127.0.0.1:8000'
worker_class = 'gaiohttp'
workers = os.cpu_count() * 2 + 1
django_settings = 'boomajoom_temp.settings'