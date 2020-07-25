import sys
sys.path.append('../')
import django,os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies_project.settings')
django.setup()
from movies.models import *

dir_path = os.path.dirname(os.path.realpath(_file_))
import json
from movies_app.models import Post
with open('p1.json') as f:
    posts_json=json.load(f)
for post in posts_json:

    post=Post.objects.create(title=post['title'],type=post['type'],cast=post['cast'])
