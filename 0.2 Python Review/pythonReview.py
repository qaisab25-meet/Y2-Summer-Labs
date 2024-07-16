def create_youtube_video(title, description):
    videosyt = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}
    }
    return videosyt

def like(youtubevideo):
    if "likes" in youtubevideo:
        youtubevideo["likes"] += 1
    return youtubevideo

def dislike(youtubevideo):
    if "dislikes" in youtubevideo:
        youtubevideo["dislikes"] += 1
    return youtubevideo

def add_comment(youtubevideo, username, comment_text):
    youtubevideo["comments"][username] = comment_text
    return youtubevideo

newyoutubevid = create_youtube_video("Python Tutorial", "Learn Python basics")
print(newyoutubevid)

newyoutubevid = like(newyoutubevid)
newyoutubevid = like(newyoutubevid)
newyoutubevid = dislike(newyoutubevid)
print(newyoutubevid)

newyoutubevid = add_comment(newyoutubevid, "user", "Great")
newyoutubevid = add_comment(newyoutubevid, "user3", "good")
print(newyoutubevid)

for  in range(496):
    newyoutubevid = like(newyoutubevid)
print(newyoutubevid)
