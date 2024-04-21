from enum import IntEnum


class Situation(IntEnum):
    ATTACKING = 0
    DEFENDING = 1
    DEFENDING_ADVANTAGE = 2
    DEFENDING_DISADVANTAGE = 3
    DEFENDING_BIG_DISADVANTAGE = 4
