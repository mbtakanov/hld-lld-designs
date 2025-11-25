from abc import ABC, abstractmethod
import re

from lld.elevator.direction import Direction
from lld.elevator.elevator import Elevator
from request import Request


class ElevatorSelectionStrategy(ABC):
    @abstractmethod
    def select_elevator(self, elevators: list[Elevator], request: Request):
        pass


class NearestElevatorStrategy(ElevatorSelectionStrategy):
    def select_elevator(self, elevators: list[Elevator], request: Request):
        best_elevator = None
        min_distance = float("inf")

        for elevator in elevators:
            if self._is_suitable(elevator, request):
                distance = abs(elevator.get_current_floor() - request.target_floor)

                if distance < min_distance:
                    min_distance = distance
                    best_elevator = elevator

        return best_elevator

    def _is_suitable(self, elevator: Elevator, request: Request) -> bool:
        if elevator.get_direction() == Direction.IDLE:
            return True

        if elevator.get_direction() == request.direction:
            if (
                request.direction == Direction.UP
                and elevator.get_current_floor() <= request.target_floor
            ):
                return True
            elif (
                request.direction == Direction.DOWN
                and elevator.get_current_floor() >= request.target_floor
            ):
                return True

        return False
