from abc import ABC
from vehicle_size import VehicleSize


class Vehicle(ABC):
    def __init__(self, lisence_number: str, size: VehicleSize):
        self.lisence_number = lisence_number
        self.size = size

    def get_lisence_number(self) -> str:
        return self.lisence_number

    def get_size(self) -> VehicleSize:
        return self.size
