import json


def get_add_posts(picture_url, content):
    with open("posts.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        post = {"pic": picture_url, "content": content}
        data.append(post)
    with open("posts.json", "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=4, ensure_ascii=False)
