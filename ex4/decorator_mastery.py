#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jay-k <jay-k@student.42.fr>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 22:59:05 by jay-k               #+#    #+#            #
#   Updated: 2026/07/24 00:01:03 by jay-k              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power:int, *args, **kwargs):
            if power >= min_power:
                return func(power, *args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(min_power=20)
def cast_spell(power: int, target: str) -> str:
    return f"Casting at {target} with {power} power"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wra


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool
    def cast_spell(self, spell_name: str, power: int) -> str





=== Exercise 4 Test Data ===
# Master's Tower Test Data
test_powers = [10, 30, 15, 12]
spell_names = ['fireball', 'freeze', 'blizzard', 'darkness']
mage_names = ['Casey', 'Rowan', 'Morgan', 'River', 'Nova', 'Kai']
invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']