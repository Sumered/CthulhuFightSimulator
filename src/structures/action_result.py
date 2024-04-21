from dataclasses import dataclass

from .action import Action
from .throw_result import ThrowResult


@dataclass
class ActionResult:
    action: Action
    result: ThrowResult
