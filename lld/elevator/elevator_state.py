from abc import ABC, abstractmethod
import re
from elevator import Elevator
from direction import Direction
from lld.elevator import request
from lld.elevator.request_source import RequestSource
from request import Request


class ElevatorState(ABC):
    @abstractmethod
    def move(self, elevator: Elevator):
        pass

    @abstractmethod
    def add_request(self, elevator: Elevator, request: Request):
        pass

    @abstractmethod
    def get_direction(self) -> Direction:
        pass


class IdleState(ElevatorState):
    def move(self, elevator: Elevator):
        if elevator.get_up_requests():
            elevator.set_state(MovingUpState())
        elif elevator.get_down_requests():
            elevator.set_state(MovingDownState())

    def add_request(self, elevator: Elevator, request: Request):
        if request.target_floor > elevator.get_current_floor():
            elevator.get_up_requests().add(request.target_floor)
        elif request.target_floor < elevator.get_current_floor():
            elevator.get_down_requests().add(request.target_floor)

    def get_direction(self) -> Direction:
        return Direction.IDLE


class MovingUpState:
    def move(self, elevator: Elevator):
        if not elevator.get_up_requests():
            elevator.set_state(IdleState())
            return

        next_floor = max(elevator.get_up_requests())
        elevator.set_current_floor(elevator.get_current_floor + 1)

        if elevator.get_current_floor == next_floor:
            print(f"Elevator {elevator.get_id()} stopped at {next_floor}")
            elevator.get_up_requests().remove(next_floor)

        if not elevator.get_up_requests():
            elevator.set_state(IdleState())

    def add_request(self, elevator: Elevator, request: Request):
        if request.source == RequestSource.INTERNAL:
            if request.target_floor > elevator.get_current_floor():
                elevator.get_up_requests().add(request.target_floor)
            else:
                elevator.get_down_requests().add(request.target_floor)
            return

        if (
            request.direction == Direction.UP
            and request.target_floor >= elevator.current_floor()
        ):
            elevator.get_up_requests().add(request.target_floor)
        elif request.direction == Direction.DOWN:
            elevator.get_down_requests().add(request.target_floor)

    def get_direction(self) -> Direction:
        return Direction.UP


class MovingDownState(ElevatorState):
    def move(self, elevator: Elevator):
        if not elevator.get_down_requests():
            elevator.set_state(IdleState())
            return

        next_floor = max(elevator.get_down_requests())
        elevator.set_current_floor(elevator.get_current_floor - 1)

        if elevator.get_current_floor == next_floor:
            print(f"Elevator {elevator.get_id()} stopped at {next_floor}")
            elevator.get_down_requests().remove(next_floor)

        if not elevator.get_down_requests():
            elevator.set_state(IdleState())

    def add_request(self, elevator: Elevator, request: Request):
        if request.source == RequestSource.INTERNAL:
            if request.target_floor > elevator.get_current_floor():
                elevator.get_up_requests().add(request.target_floor)
            else:
                elevator.get_down_requests().add(request.target_floor)
            return

        if (
            request.direction == Direction.DOWN
            and request.target_floor <= elevator.current_floor()
        ):
            elevator.get_down_requests().add(request.target_floor)
        elif request.direction == Direction.UP:
            elevator.get_up_requests().add(request.target_floor)

    def get_direction(self) -> Direction:
        return Direction.DOWN
