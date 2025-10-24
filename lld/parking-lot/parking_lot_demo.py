from parking_lot import ParkingLot
from parking_floor import ParkingFloor
from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_size import VehicleSize
from fee_strategy import FlatRateStrategy, VehicleBaseFeeStrategy
from bike import Bike
from car import Car
from truck import Truck

class ParkingLotDemo:
    @staticmethod
    def main():
        parking_lot = ParkingLot.get_instance()

        # 1. Init the parking lot with floors and spots
        floor1 = ParkingFloor(1)
        floor1.add_spot(ParkingSpot("F1-S1", VehicleSize.SMALL))
        floor1.add_spot(ParkingSpot("F1-M1", VehicleSize.MEDIUM))
        floor1.add_spot(ParkingSpot("F1-L1", VehicleSize.SMALL))

        floor2 = ParkingFloor(2)
        floor2.add_spot(ParkingSpot("F2-M1", VehicleSize.MEDIUM))
        floor2.add_spot(ParkingSpot("F2-M2", VehicleSize.MEDIUM))


        parking_lot.add_floor(floor1)
        parking_lot.add_floor(floor2)
        parking_lot.set_fee_strategy(VehicleBaseFeeStrategy())

        print('\n--- Vehicle Entries ---')
        floor1.display_availability()
        floor2.display_availability()

        bike = Bike("B-123")
        car = Car("C-456")
        truck = Truck("T-789")
        
        bike_ticket = parking_lot.park_vehicle(bike)
        car_ticket = parking_lot.park_vehicle(car)
        truck_ticket = parking_lot.park_vehicle(truck)

        print('\n--- Vehicle Entries ---')
        floor1.display_availability()
        floor2.display_availability()

        bike2 = Bike("C-999")
        bike2_ticket = parking_lot.park_vehicle(bike2)
        car2 = Car("C-999")
        car2_ticket = parking_lot.park_vehicle(car2)


if __name__ == "__main__":
    ParkingLotDemo.main()

