import numpy as np


class DiceService:
    __randomizer = np.random.default_rng()

    @staticmethod
    def d100() -> int:
        return int(DiceService.__randomizer.uniform(1, 100))

    @staticmethod
    def d10() -> int:
        return int(DiceService.__randomizer.uniform(1, 10))

    @staticmethod
    def d8() -> int:
        return int(DiceService.__randomizer.uniform(1, 8))

    @staticmethod
    def d4() -> int:
        return int(DiceService.__randomizer.uniform(1, 4))

    @staticmethod
    def d3() -> int:
        return int(DiceService.__randomizer.uniform(1, 3))
