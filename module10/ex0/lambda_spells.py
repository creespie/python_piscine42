def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda dic: dic["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda dic: dic["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    stats = {}
    stats["max_power"] = max(mages, key=lambda mags: mags["power"])["power"]
    stats["min_power"] = min(mages, key=lambda mags: mags["power"])["power"]
    stats["avg_power"] = round(sum(mags["power"] for mags in mages) / len(mages), 2)
    return stats


def main():
    artifacts = [
        {"name": "Earth Shield", "power": 111, "type": "accessory"},
        {"name": "Light Prism", "power": 106, "type": "accessory"},
        {"name": "Ice Wand", "power": 96, "type": "weapon"},
        {"name": "Storm Crown", "power": 63, "type": "relic"},
    ]

    mages = [
        {"name": "Jordan", "power": 100, "element": "ice"},
        {"name": "Riley", "power": 78, "element": "fire"},
        {"name": "Jordan", "power": 96, "element": "shadow"},
        {"name": "Ember", "power": 77, "element": "water"},
        {"name": "Jordan", "power": 96, "element": "ice"},
    ]

    spells = ["darkness", "blizzard", "tornado", "heal"]

    print("=== artifact_sorter ===")
    for a in artifact_sorter(artifacts):
        print(a)

    print("\n=== power_filter (min_power=90) ===")
    for m in power_filter(mages, 90):
        print(m)

    print("\n=== spell_transformer ===")
    for s in spell_transformer(spells):
        print(s)

    print("\n=== mage_stats ===")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
