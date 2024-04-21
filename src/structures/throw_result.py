from enum import IntEnum


class ThrowResult(IntEnum):
    FAILURE = 0
    SUCCESS = 1

    GREAT_SUCCESS = 2
    ULTRA_SUCCESS = 3
    CRITICAL_SUCCESS = 1000
    CRITICAL_FAILURE = -1000
