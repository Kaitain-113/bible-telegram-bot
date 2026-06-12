from dataclasses import dataclass
from typing import Callable, Optional

from .handlers import (
    get_versicle,
)


@dataclass(frozen=True)
class CommandSpecification:
    trigger: str
    action: Callable[..., None]
    description: Optional[str]


class CommandRegistry:
    GET_VERSICLE = CommandSpecification(
        trigger='v', action=get_versicle, description='Get a bible versicle'
    )
