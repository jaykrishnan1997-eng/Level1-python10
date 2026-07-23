#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   functools_artifacts.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jay-k <jay-k@student.42.fr>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 19:09:42 by jay-k               #+#    #+#            #
#   Updated: 2026/07/23 22:29:20 by jay-k              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from functools import reduce, lru_cache, partial, singledispatch
from operator import add, mul
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return reduce(add, spells)
    if operation == "multiply":
        return reduce(mul, spells)
    if operation == "max":
        return reduce(max, spells)
    if operation == "min":
        return reduce(min, spells)
    raise ValueError(f"Unknown operation: {operation}")


def enchant_item(power: int, element: str, target: str) -> str:
    return f"{element} enchantment ({power} power) applied to {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire_enchant': partial(base_enchantment, power=50, element="fire"),
        'ice_enchant': partial(base_enchantment, power=50, element="ice"),
        'shadow_enchant': partial(base_enchantment, power=50, element="shadow"),
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(i: int) -> int:
    if i <= 1:
        return i
    return memoized_fibonacci(i - 1) + memoized_fibonacci(i - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    # Ancient Library Test Data
    spell_powers = [46, 40, 11, 42, 30, 17]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [12, 15, 19]

    print("Testing spell reducer...")
    for op in operations:
        result = spell_reducer(spell_powers, op)
        print(f"{op.capitalize()}: {result}")

    print("\nTesting partial enchanter...")
    enchants = partial_enchanter(enchant_item)
    print(enchants['fire_enchant'](target="Sword"))
    print(enchants['ice_enchant'](target="Shield"))
    print(enchants['shadow_enchant'](target="Cloak"))
    print("\n")
    print("Testing memoized fibonacci...")
    for n in fibonacci_tests:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(memoized_fibonacci.cache_info())
    print("\n")
    print("Testing spell dispatcher...")
    caster = spell_dispatcher()
    print(caster(42))
    print(caster("fireball"))
    print(caster([3, 5, 4]))
    print(caster(2.22))
