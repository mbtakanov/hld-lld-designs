import threading
import time


class Elevator:
    def __init__(self, id: str, capacity: int):
        self.id = id
        self.capacity = capacity
        self.current_floor = 1
        self.current_floor_lock = threading.Lock()
        self.is_running = True
        self.up_requests = set()
        self.down_requests = set()

        # Observer Pattern: List of observers
        self.observers = []

    def run(self):
        while self.is_running:
            self.move()
            try:
                time.sleep(1)  # Simulate movement time
            except KeyboardInterrupt:
                self.is_running = False
                break
