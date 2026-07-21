#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   higher_magic.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jay-k <jay-k@student.42.fr>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 21:10:20 by jay-k               #+#    #+#            #
#   Updated: 2026/07/21 23:49:02 by jay-k              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def checker(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return checker


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str, power: int) -> list:
        return [s(target, power) for s in spells]
    return cast_all


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

if __name__ == "__main__":
    test_values = [22, 7, 7]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result}")
    print("\n")

#     print("\nTesting power amplifier...")
# mega_fireball = power_amplifier(fireball, 3)
# original = fireball(test_targets[0], test_values[0])
# amplified = mega_fireball(test_targets[0], test_values[0])
# print(f"Original: {original}")
# print(f"Amplified: {amplified}")

# def is_powerful(target: str, power: int) -> bool:
#     return power >= 20