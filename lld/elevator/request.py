from dataclasses import dataclass

from direction import Direction
from request_source import RequestSource


@dataclass
class Request:
    target_floor: int
    direction: Direction
    source: RequestSource

    def __str__(self):
        if self.source == RequestSource.EXTERNAL:
            return f"{self.source.value} request to floor {self.target_floor} going {self.direction.value}"
        else:
            return f"{self.source.value} request to floor {self.target_floor}"
