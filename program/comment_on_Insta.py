from instagrapi import Client
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("Instagram_USERNAME")
password = os.getenv("Instagram_PASSWORD")

cl = Client()

try:
    cl.load_settings("session.json")
except:
    pass

cl.login(username, password)

cl.dump_settings("session.json")

# cl = Client()

# cl.login(username, password)

username = "mario.code.lab"

# Get user ID
user_id = cl.user_id_from_username(username)

# Get most recent post
media = cl.user_medias(user_id, amount=1)[0]

# Comment on the post
cl.media_comment(media.id, "Great post!")