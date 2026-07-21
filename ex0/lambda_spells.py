#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   lambda_spells.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 15:45:51 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/21 16:25:16 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mage: list[dict]) -> dict:
    numbers = [m['power'] for m in mage]
    max_value = max(mage, key=lambda x: x['power'])['power']
    min_value = min(mage, key=lambda x: x['power'])['power']
    av_value = round(sum(numbers)/len(numbers), 2)
    return {'max_power': max_value, 'min_power': min_value, 'avg_power': av_value}


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 100, 'type': 'relic'},
        {'name': 'Ice Wand', 'power': 100, 'type': 'relic'},
        {'name': 'Wind Cloak', 'power': 120, 'type': 'armor'},
        {'name': 'Shadow Blade', 'power': 69, 'type': 'relic'}
    ]

    mages = [
        {'name': 'Sage', 'power': 100, 'element': 'shadow'},
        {'name': 'Riley', 'power': 96, 'element': 'ice'},
        {'name': 'Alex', 'power': 97, 'element': 'shadow'},
        {'name': 'Ash', 'power': 50, 'element': 'lightning'},
        {'name': 'Luna', 'power': 87, 'element': 'fire'}
    ]

    spells = ['shield', 'darkness', 'earthquake', 'tornado']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    count = 0
    for a in sorted_artifacts:
        count += 1
        print(f"{a['name']} ({a['power']} power)", end="")
        if count < len(sorted_artifacts):
            print(" comes before", end=" ")
    print("\n\nTesting spell transformer...")
    mapped_spells = spell_transformer(spells)
    for b in mapped_spells:
        print(b, end=" ")
    print("\n")
    print("Testing power filter (min_power = 90)...")
    filtered = power_filter(mages, 90)
    print(", ".join(m['name'] for m in filtered))
    print("\n")
    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(stats)
