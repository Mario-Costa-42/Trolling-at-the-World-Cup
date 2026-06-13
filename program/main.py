from bs4 import BeautifulSoup
import re
import subprocess

TEAM_NAME = input("Qual seleção vai ser moggada: ")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

heading = soup.find(
    lambda tag: tag.name == "h2" and TEAM_NAME.lower() in tag.get_text().lower()
)

if not heading:
    print(f"Team '{TEAM_NAME}' not found.")
    exit()

squad = {}

for element in heading.find_next_siblings():

    if element.name == "h2":
        break

    if element.name != "p":
        continue

    strong = element.find("strong")
    if not strong:
        continue

    position = strong.get_text(strip=True).replace(":", "")

    text = element.get_text(" ", strip=True)
    players_text = re.sub(
        rf"^{re.escape(strong.get_text(strip=True))}\s*", "", text
    )

    players = [player.strip() for player in players_text.split("·")]

    squad[position] = players

# Run next_script.py for every player
for position, players in squad.items():
    for player in players:
        subprocess.run(
            ["python", "test.py", TEAM_NAME, position, player],
            check=True
        )