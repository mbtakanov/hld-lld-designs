import threading
from typing import Dict
from parking_spot import ParkingSpot


class ParkingFloor:
    def __init__(self, floor_number: int):
        self.floor_number = floor_number
        self.splots: Dict[str, ParkingSpot] = {}
        self._lock = threading.Lock()

    def add_spot(self, spot: ParkingSpot):
        return 1
