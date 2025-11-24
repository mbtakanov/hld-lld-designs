from abc import ABC, abstractmethod

from elevator import Elevator


class ElevatorObserver(ABC):
    @abstractmethod
    def update(self, elevator: Elevator):
        pass


class Dispaly(ElevatorObserver):
    def update(self, elevator: Elevator):
        print(
            f"[DISPLAY] Elevator {elevator.get_id()} | Current Floor: {elevator.get_current_floor()} | Direction: {elevator.get_direction().value}"
        )
