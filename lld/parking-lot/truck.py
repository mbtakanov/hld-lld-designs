from vehicle import Vehicle
from vehicle_size import VehicleSize


class Truck(Vehicle):
    def __init__(self, lisence_number: str):
        super().__init__(lisence_number, VehicleSize.LARGE)
