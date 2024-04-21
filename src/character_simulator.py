from .structures import Action, ActionResult, Character, Situation, Strategy, ThrowResult
from .throw_result_service import ThrowResultService


class CharacterSimulator:
    def __init__(self, character: Character, strategy: Strategy) -> None:
        self.__strategy = strategy
        self.__character = character

    def action(self, situation: Situation) -> ActionResult:
        if situation == Situation.ATTACKING:
            result = self.__handle_attack()
            return result
        else:
            result = self.__handle_defending(situation)
            return result

    def __handle_attack(self) -> ActionResult:
        if self.__strategy in [Strategy.OFFENSIVE, Strategy.BALANCED]:
            throw_result = ThrowResultService.get_normal_result(self.__character.fighting)
            return ActionResult(Action.ATTACK, throw_result)
        else:
            return ActionResult(Action.NONE, ThrowResult.SUCCESS)

    def __handle_defending(self, situation: Situation) -> ActionResult:
        if self.__strategy in [Strategy.OFFENSIVE, Strategy.COUNTER_ONLY]:
            throw_result = ThrowResultService.get_normal_result(self.__character.fighting)
            return ActionResult(Action.COUNTER, throw_result)
        else:
            if situation == Situation.DEFENDING:
                throw_result = ThrowResultService.get_normal_result(self.__character.dodge)
                return ActionResult(Action.DEFEND, throw_result)
            elif situation == Situation.DEFENDING_DISADVANTAGE:
                throw_result = ThrowResultService.get_disadvantage_result(self.__character.dodge)
                return ActionResult(Action.DEFEND, throw_result)
            elif situation == Situation.DEFENDING_ADVANTAGE:
                throw_result = ThrowResultService.get_advantage_result(self.__character.dodge)
                return ActionResult(Action.DEFEND, throw_result)
            else:
                throw_result = ThrowResultService.get_double_disadvantage_result(self.__character.dodge)
                return ActionResult(Action.DEFEND, throw_result)

    def get_damage(self) -> int:
        damage = 0
        for dice in self.__character.damage:
            damage += dice()
        return int(damage)

    def is_dead(self) -> bool:
        return self.__character.health_points <= 0
