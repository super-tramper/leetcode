class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        self.parking[carType] -= 1
        return self.parking[carType] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
if __name__ == "__main__":
    obj = ParkingSystem(1,1,0)
    print(obj.addCar(1))
    print(obj.addCar(2))
    print(obj.addCar(3))
    print(obj.addCar(1))