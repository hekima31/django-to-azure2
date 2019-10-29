import json
from blog.models import Post
with open("posts.json") as f:
    posts_json=json.load(f) #converts from json to dict

#     i=0

    
# for post in posts_json:
#     print(post["user_id"])


# # dict_sample={"user_1":"Hope","user_2":52,"user_3":"Anastasia","user_4":"Stella"}
# # print("This is dictionary")
# # print(dict_sample)

for post in posts_json:
    post=Post(title=post["title"],content=post["content"],author_id=post["user_id"])
    post.save()