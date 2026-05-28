#!/usr/bin/env python3
import typing
from ..ex0 import *
from ..ex1 import *
from .ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy

def battle(battles_creatures: list[tuple[typing.Any, typing.Any]]):
    #--------------Print Battle List-----------------------#
    print('[',end='')
    i = 1
    for creature_strategy in battles_creatures:
        print(f'{creature_strategy[0]}+{creature_strategy[1]})', end='')
        if i != len(battles_creatures):
            print(',',end='')
        i += 1
    print(']')
    print(*** Tournament ***)
    print(f"{????} opponents involved")

    #---------------*BATTLE*--------------------------------#
    print("* Battle *")
    
    
        
if __name__ == "__main__":
    #-------Creating Creature---------#
    Healing = HealingCreatureFactory
    Transform = TransformCreatureFactory
    Flaming = FlameFactory
    Aquabub = AquaFactory
    
    #-------Creating Strategies-------#
    Normal = NormalStrategy
    Aggressive = AggressiveStrategy
    Defensive = DefensiveStrategy
    
    #-------Battle--------------------#
    
    