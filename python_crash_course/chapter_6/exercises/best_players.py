best_players = {
    'noah': ['joe burrow', 'jaylen waddle', 'drake london'],
    'brad': ['bijan robinson', 'kyler murray', 'garrett wilson'],
    'tommy': ['lamar jackson', 'devonta smith', 'jordan love'],
    'connor': ['josh allen', 'jonathan taylor', "de'von achane"]
}

print("I have the first round picks belonging to")
for name in best_players.keys():
    print(f"\t{name.title()}")

for name, players in best_players.items():
    print(f"\n{name.title()}'s best players are")
    for player in players:
        print(f"\t{player.title()}")
