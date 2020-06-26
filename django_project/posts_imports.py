import json
from blog.models import Post

with open("posts.json") as f:
    posts_json = json.load(f)

for post_var in posts_json:
    post_var = Post(
        title=post_var["title"], content=post_var["content"], author_id=post_var["user_id"])
    post_var.save()
