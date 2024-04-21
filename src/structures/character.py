from typing import Callable

from pydantic import BaseModel


class Character(BaseModel):
    dodge: int
    damage: list[Callable[[], int]]
    fighting: int
    health_points: int
