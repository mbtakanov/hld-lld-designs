from concurrent.futures import ThreadPoolExecutor
import threading

from elevator_selection_strategy import NearestElevatorStrategy
from elevator_observer import Display
from elevator import Elevator
from direction import Direction
from lld.elevator.request_source import RequestSource
from request import Request


class ElevatorSystem:
    _instance = None
    _lock = threading.lock()

    def __new__(cls, num_elevators: int):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self, num_elevators: int):
        if self._initialized:
            return

        self.selection_strategy = NearestElevatorStrategy()
        self.executor_service = ThreadPoolExecutor(max_workers=num_elevators)

        elevators = []
        display = Display()

        for i in range(1, num_elevators + 1):
            elevator = Elevator(i)
            elevator.add_observer(display)
            elevators.append(elevator)

        self.elevators = {elevator.get_id(): elevator for elevator in elevators}
        self._initialize = True

    @classmethod
    def get_instance(cls, num_elevators: int):
        return cls(num_elevators)

    def start(self):
        for elevator in self.elevators.values():
            self.executor_service.submit(elevator.run)

    def request_elevator(self, floor: int, direction: Direction):
        print(
            f"\n>> EXTERNAL Request: User at floor {floor} wants to go {direction.value}"
        )
        request = Request(floor, direction, RequestSource.EXTERNAL)

        selected_elevator = self.selection_strategy.select_elevator(
            list(self.elevators.values()), request
        )

        if selected_elevator:
            selected_elevator.add_request(request)
        else:
            print("System is busy, please wait.")

    # def select_floor(self, elevator_id: int, destination_floor: int):

