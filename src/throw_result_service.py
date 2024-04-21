from .dice_service import DiceService
from .structures.throw_result import ThrowResult


class ThrowResultService:

    @staticmethod
    def __get_result(throw_value: int, stat_value: int) -> ThrowResult:
        if throw_value == 100:
            return ThrowResult.CRITICAL_FAILURE
        elif throw_value > stat_value:
            return ThrowResult.FAILURE
        elif throw_value == 1:
            return ThrowResult.CRITICAL_SUCCESS
        else:
            if throw_value <= stat_value // 4:
                return ThrowResult.ULTRA_SUCCESS
            elif throw_value <= stat_value // 2:
                return ThrowResult.GREAT_SUCCESS
            return ThrowResult.SUCCESS

    @staticmethod
    def get_normal_result(stat_value: int) -> ThrowResult:
        throw_value = DiceService.d100()

        return ThrowResultService.__get_result(throw_value, stat_value)

    @staticmethod
    def get_advantage_result(stat_value: int) -> ThrowResult:
        first_throw, second_throw = DiceService.d100(), DiceService.d100()
        throw_value = min(first_throw, second_throw)

        return ThrowResultService.__get_result(throw_value, stat_value)

    @staticmethod
    def get_disadvantage_result(stat_value: int) -> ThrowResult:
        first_throw, second_throw = DiceService.d100(), DiceService.d100()
        throw_value = max(first_throw, second_throw)

        return ThrowResultService.__get_result(throw_value, stat_value)

    @staticmethod
    def get_double_disadvantage_result(stat_value: int) -> ThrowResult:
        first_throw, second_throw, third_throw = DiceService.d100(), DiceService.d100(), DiceService.d100()
        throw_value = max(first_throw, second_throw, third_throw)

        return ThrowResultService.__get_result(throw_value, stat_value)
