import json

with open('posts.json') as f:
    posts_json=json.load(f)
for posts in posts_json:
    print(posts['title'])
