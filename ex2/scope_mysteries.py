#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   scope_mysteries.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jay-k <jay-k@student.42.fr>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/22 16:56:09 by jay-k               #+#    #+#            #
#   Updated: 2026/07/23 15:02:10 by jay-k              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def power_accumulator(amount: int) -> int:
        nonlocal total_power
        total_power = total_power + amount
        return total_power
    return power_accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply_enchantment


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value) -> None:
        memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    # Memory Depths Test Data
    initial_powers = [44, 53, 35]
    power_additions = [8, 9, 15, 17, 8]
    enchantment_types = ['Earthen', 'Flaming', 'Dark']
    items_to_enchant = ['Ring', 'Shield', 'Cloak', 'Wand']

    counter_a = mage_counter()
    counter_b = mage_counter()
    result1 = counter_a()
    print(f"counter_a call 1: {result1}")
    result2 = counter_a()
    print(f"counter_a call 2: {result2}")
    result3 = counter_b()
    print(f"counter_b call 1: {result3}")
    accumulator = spell_accumulator(initial_powers[0])
    r1 = accumulator(power_additions[0])
    print(f"Base {initial_powers[0]}, add {power_additions[0]}: {r1}")
    r2 = accumulator(power_additions[1])
    print(f"Base {initial_powers[0]}, add {power_additions[1]}: {r2}")
    print("\n")
    earthen_enchant = enchantment_factory(enchantment_types[0])
    flaming_enchant = enchantment_factory(enchantment_types[1])
    result4 = earthen_enchant(items_to_enchant[0])
    result5 = flaming_enchant(items_to_enchant[1])
    print(result4)
    print(result5)
    print("\n")
    print("Testing memory_vault...")
    vault = memory_vault()
    vault['store'](items_to_enchant[0], power_additions[0])
    result6 = vault['recall'](items_to_enchant[0])
    print(f"Recall '{items_to_enchant[0]}': {result6}")

    missing = vault['recall']('unknown')
    print(f"Recall 'unknown': {missing}")
