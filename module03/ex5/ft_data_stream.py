import random
import typing

def gen_event() -> typing.Generator[tuple[str,str], None, None]:
    while True:
        actions = ["run", "sleep", "climb", "grab", "sleep", "move", "release"]
        players = ["bob", "alice", "dylan", "charlie"]
        name = random.choice(players)
        chosen_action = random.choice(actions)
        yield (name, chosen_action)

if __name__ == "__main__":
    gen = gen_event()
    for i in range(0, 1000):
        print(f"{i}: {next(gen)}")
    list_of_ten =[]
    for _ in range(0, 10):
        list_of_ten.append(next(gen))
    print(f"Built list of 10 events: {list_of_ten}")
    for _ in range(0, 10):
        to_remove = random.choice(list_of_ten)
        print(f"Got event from list: {to_remove}")
        list_of_ten.remove(to_remove)
        print(f"Remains in list: {list_of_ten}")