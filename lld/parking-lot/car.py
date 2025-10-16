from vehicle import Vehicle
from vehicle_size import VehicleSize


class Car(Vehicle):
    def __init__(self, lisence_number: str):
        super().__init__(lisence_number, VehicleSize.MEDIUM)
