# from instagrapi import Client
# from dotenv import load_dotenv
# import os
# import time
# import random
# import sys

# load_dotenv()

# COMMENTS_Received = sys.argv[1]
# COMMENTS = [comment.strip() for comment in COMMENTS_Received.split("****")]

# INSTAGRAM_TARGET = sys.argv[2]

# print(COMMENTS)

# username = os.getenv("Instagram_USERNAME")
# password = os.getenv("Instagram_PASSWORD")

# cl = Client()

# try:
#     cl.load_settings("session.json")
# except Exception:
#     pass

# cl.login(username, password)
# time.sleep(random.randint(5, 15))
# cl.dump_settings("session.json")

# # Get user ID
# user_id = cl.user_id_from_username(INSTAGRAM_TARGET)

# # Get most recent post
# media = cl.user_medias(user_id, amount=1)[0]

# # Post comments one by one
# for i, comment in enumerate(COMMENTS, start=1):
#     try:
#         cl.media_comment(media.id, comment)
#         print(f"[{i}/{len(COMMENTS)}] Comment posted.")

#         if i < len(COMMENTS):
#             delay = random.randint(180, 600)
#             print(f"Waiting {delay} seconds...")
#             time.sleep(delay)

#     except Exception as e:
#         print(f"Error posting comment {i}: {e}")



















































# from instagrapi import Client
# from dotenv import load_dotenv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import os
# import time
# import random
# import sys

# load_dotenv()

# COMMENTS_Received = sys.argv[1]
# COMMENTS = [comment.strip() for comment in COMMENTS_Received.split("****")]
# INSTAGRAM_TARGET = sys.argv[2]

# print(COMMENTS)

# username = os.getenv("Instagram_USERNAME")
# password = os.getenv("Instagram_PASSWORD")

# # -------------------------
# # Login with instagrapi
# # -------------------------
# cl = Client()

# try:
#     cl.load_settings("session.json")
# except Exception:
#     pass

# cl.login(username, password)
# print(cl.user_id)
# print(cl.username)
# time.sleep(random.randint(5, 15))
# cl.dump_settings("session.json")

# # -------------------------
# # Get latest post with Selenium
# # -------------------------
# options = Options()

# # Uncomment if you want headless mode
# # options.add_argument("--headless=new")

# driver = webdriver.Chrome(options=options)

# try:
#     profile_url = f"https://www.instagram.com/{INSTAGRAM_TARGET}/"
#     driver.get(profile_url)

#     # Give the page time to load
#     time.sleep(random.randint(4, 7))

#     # Find the first post link
#     post = driver.find_element(By.CSS_SELECTOR, "a[href*='/p/']")
#     post_url = post.get_attribute("href")

#     print(f"Latest post: {post_url}")

#     # Extract shortcode
#     shortcode = post_url.split("/p/")[1].split("/")[0]
#     print(f"Shortcode: {shortcode}")

# finally:
#     driver.quit()

# # -------------------------
# # Convert shortcode to media PK
# # -------------------------
# media_pk = cl.media_pk_from_code(shortcode)

# # -------------------------
# # Post comments one by one
# # -------------------------
# for i, comment in enumerate(COMMENTS, start=1):
#     try:
#         cl.media_comment(media_pk, comment)
#         print(f"[{i}/{len(COMMENTS)}] Comment posted.")

#         if i < len(COMMENTS):
#             delay = random.randint(180, 600)
#             print(f"Waiting {delay} seconds...")
#             time.sleep(delay)

#     except Exception as e:
#         print(f"Error posting comment {i}: {e}")













from instagrapi import Client
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
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

# -------------------------
# Login with instagrapi
# -------------------------
cl = Client()

try:
    cl.load_settings("session.json")
except Exception:
    pass

cl.login(username, password)

print(f"Logged in as: {cl.username}")
print(f"User ID: {cl.user_id}")

time.sleep(random.randint(5, 15))
cl.dump_settings("session.json")

# -------------------------
# Get latest post with Selenium
# -------------------------
options = Options()

# Uncomment if desired
# options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

shortcode = None

try:
    profile_url = f"https://www.instagram.com/{INSTAGRAM_TARGET}/"
    print(f"Opening {profile_url}")

    driver.get(profile_url)

    posts = WebDriverWait(driver, 90).until(
        lambda d: d.find_elements(
            By.CSS_SELECTOR,
            "a[href*='/p/'], a[href*='/reel/']"
        )
    )

    if not posts:
        raise Exception(f"No posts found for {INSTAGRAM_TARGET}")

    post_url = posts[0].get_attribute("href")
    print(f"Latest post: {post_url}")

    if "/p/" in post_url:
        shortcode = post_url.split("/p/")[1].split("/")[0]
    elif "/reel/" in post_url:
        shortcode = post_url.split("/reel/")[1].split("/")[0]
    else:
        raise Exception(f"Could not extract shortcode from {post_url}")

    print(f"Shortcode: {shortcode}")

except TimeoutException:
    print("Timed out waiting for posts.")
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)

    driver.save_screenshot("instagram_error.png")
    print("Screenshot saved as instagram_error.png")

    sys.exit(1)

except Exception as e:
    print("Error while getting latest post:", e)
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)

    driver.save_screenshot("instagram_error.png")
    print("Screenshot saved as instagram_error.png")

    sys.exit(1)

finally:
    driver.quit()

# -------------------------
# Convert shortcode to media PK
# -------------------------
try:
    media_pk = cl.media_pk_from_code(shortcode)
except Exception as e:
    print(f"Failed to convert shortcode: {e}")
    sys.exit(1)

# -------------------------
# Post comments one by one
# -------------------------
for i, comment in enumerate(COMMENTS, start=1):
    try:
        cl.media_comment(media_pk, comment)
        print(f"[{i}/{len(COMMENTS)}] Comment posted.")

        if i < len(COMMENTS):
            delay = random.randint(180, 600)
            print(f"Waiting {delay} seconds...")
            time.sleep(delay)

    except Exception as e:
        print(f"Error posting comment {i}: {e}")