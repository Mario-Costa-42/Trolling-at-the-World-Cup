from instagrapi import Client
from dotenv import load_dotenv
import os
import time
import random
import sys

load_dotenv()

COMMENTS_Received = sys.argv[1]
COMMENTS = [comment.strip() for comment in COMMENTS_Received.split("****")]

INSTAGRAM_TARGET = sys.argv[2]

print(COMMENTS)

username = os.getenv("Instagram_USERNAME")
password = os.getenv("Instagram_PASSWORD")

cl = Client()

try:
    cl.load_settings("session.json")
except Exception:
    pass

cl.login(username, password)
time.sleep(random.randint(5, 15))
cl.dump_settings("session.json")

# Get user ID
user_id = cl.user_id_from_username(INSTAGRAM_TARGET)

# Get most recent post
media = cl.user_medias(user_id, amount=1)[0]

# Post comments one by one
for i, comment in enumerate(COMMENTS, start=1):
    try:
        cl.media_comment(media.id, comment)
        print(f"[{i}/{len(COMMENTS)}] Comment posted.")

        if i < len(COMMENTS):
            delay = random.randint(180, 600)
            print(f"Waiting {delay} seconds...")
            time.sleep(delay)

    except Exception as e:
        print(f"Error posting comment {i}: {e}")


