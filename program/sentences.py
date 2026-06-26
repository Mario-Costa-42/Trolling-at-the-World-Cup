import sys
from openai import OpenAI
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

#Variables
nation = sys.argv[1]
position = sys.argv[2][:-1]
player = sys.argv[3]
Out_of_Cup = sys.argv[4]
players_insta = sys.argv[5]

client = OpenAI(api_key=api_key)

prompt = f"""

You are a football Twitter troll with encyclopedic knowledge of the sport. 
Your task is to roast a player whose national team has just been eliminated from the FIFA World Cup.
Player: {player}
Country: {nation}
Stage of elimination: {Out_of_Cup}
Rules:
* Write 5 roasts.
* Sound like football Twitter/X banter. 
* Be creative, very sarcastic, and meme-worthy. 
* Focus on football performance, results, hype, expectations, and tournament failure.
* Mix different styles: fake stats, comparisons, jokes, one-liners, and "finished player" allegations.
* Keep each roast under 25 words.
* Make them sound like comments people would post under an Instagram post after the elimination. 
* Output only the roasts, one per line with quotation marks on them and four **** separating them.
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

print("\nRoasts:\n")
print(response.output_text)
print(type(response.output_text))

subprocess.run(["python", "comment_on_Insta.py", response.output_text, players_insta])

