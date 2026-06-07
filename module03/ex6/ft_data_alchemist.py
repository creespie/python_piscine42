import random


def data_manager() -> None:
    players_original = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    player_converted = []
    player_capitalized = []
    for player in players_original:
        player_converted.append(player.capitalize())
    for player in players_original:
        if player == player.capitalize():
            player_capitalized.append(player)
    print(f"Initial list of players: {players_original}")
    print(f"New list with all names capitalized:  {player_converted}")
    print(f"New list of capitalized names only: {player_capitalized}")
    first_dict = {name: random.randint(0, 1000) for name in player_converted}
    print(f"Score dict: {first_dict}")
    total = 0
    for score in first_dict.values():
        total += score
    average = round(total / len(first_dict), 2)
    print(f"Score average is {average}")
    higher_dict = {name: value for name, value in first_dict.items() if value > average}
    print(f"High scorre: {higher_dict}")


if __name__ == "__main__":
    data_manager()