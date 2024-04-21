from pydantic import BaseModel


class StrategyResults(BaseModel):
    class Results(BaseModel):
        wins: int = 0
        turns: int = 0
        losses: int = 0

    balanced = Results()
    defensive = Results()
    offensive = Results()
    only_counter = Results()
