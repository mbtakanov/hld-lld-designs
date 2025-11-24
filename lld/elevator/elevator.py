import time
import threading

from request import Request
from direction import Direction
from elevator_observer import ElevatorObserver
from elevator_state import ElevatorState, IdleState


class Elevator:
    def __init__(self, id: str, capacity: int):
        self.id = id
        self.capacity = capacity
        self.current_floor = 1
        self.current_floor_lock = threading.Lock()
        self.state = IdleState()
        self.is_running = True
        self.up_requests = set()
        self.down_requests = set()

        self.observers: list[ElevatorObserver] = []

    def add_observer(self, observer: ElevatorObserver):
        self.observers.append(observer)
        observer.update(self)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def set_state(self, state: ElevatorState):
        self.state = state
        self.notify_observers()

    def move(self):
        self.state.move(self)

    def add_request(self, request: Request):
        print(f"Elevator {self.id} proccesing: {request}")
        self.state.add_request(self, request)

    def get_id(self):
        return self.id

    def get_current_floor(self):
        with self.current_floor_lock:
            return self.current_floor

    def set_current_floor(self, floor: int):
        with self.current_floor_lock:
            self.current_floor = floor
        self.notify_observers()

    def get_direction(self) -> Direction:
        return self.state.get_direction()

    def get_up_requests(self) -> set[int]:
        return self.up_requests

    def get_down_requests(self) -> set[int]:
        return self.down_requests

    def is_elevator_running(self):
        return self.is_running

    def stop_elevator(self):
        self.is_running = False

    def run(self):
        while self.is_running:
            self.move()
            try:
                time.sleep(1)  # Simulate movement time
            except KeyboardInterrupt:
                self.is_running = False
                break
