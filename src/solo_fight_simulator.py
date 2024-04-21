from .character_simulator import CharacterSimulator
from .rules.rules_interpreter import RulesInterpreter
from .structures.character import Character
from .structures.strategy_results import StrategyResults


class SoloFightSimulator:

    def __init__(self, simulation_iterations: int, rules_interpreter: RulesInterpreter) -> None:
        self.__iterations = simulation_iterations

    def simulate(self, hero: Character, enemy: Character) -> StrategyResults:
        results = StrategyResults()

        return results

    def __fight_simulation(self, hero: CharacterSimulator, enemy: CharacterSimulator) -> StrategyResults.Results:
        results = StrategyResults.Results()

        return results
