import subprocess
import sys
import search_player

nation = sys.argv[1]
position = sys.argv[2][:-1]
player = sys.argv[3]
Out_of_Cup = sys.argv[4]

players_insta = search_player.find_instagram_username(player)
print(players_insta)

print(f"Nation: {nation}")
print(f"Position: {position}")
print(f"Player: {player}")
print(f"Out of Cup: {Out_of_Cup}")

subprocess.run(["python", "sentences.py", nation, position, player, Out_of_Cup, players_insta])