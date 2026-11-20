class Vehicle:
    """Represents a vehicle with a read-only mileage."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Initializes a vehicle with zero mileage."""
        self.make = make
        self.model = model
        self.year = year
        self._mileage: float = 0

    @property
    def mileage(self) -> float:
        """Returns the total distance traveled in kilometers."""
        return self._mileage

    def drive(self, km: float) -> None:
        """Increases mileage by a positive distance."""
        if not km > 0:
            raise ValueError("Distance must be greater than 0")

        self._mileage += km
        print(f"{self.make} {self.model}: traveled {km:g} km")

    def refuel(self, liters: float) -> None:
        """Requires subclasses to provide their refueling behavior."""
        raise NotImplementedError("Refueling must be implemented by a specific vehicle type")

    def status(self) -> str:
        """Returns the vehicle details and current mileage."""
        return (
            f"{self.make} {self.model}, {self.year}; "
            f"mileage: {self.mileage:g} km"
        )

    def __repr__(self) -> str:
        """Returns a technical representation of the vehicle."""
        return (
            f"{type(self).__name__}("
            f"make={self.make!r}, model={self.model!r}, year={self.year})"
        )


class Car(Vehicle):
    """Represents a car that consumes fuel while driving."""

    FUEL_CONSUMPTION: float = 8.0

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        fuel_type: str,
        fuel_level: float = 0,
    ) -> None:
        """Initializes a car with its fuel type and fuel level in liters."""
        super().__init__(make, model, year)

        if not fuel_level >= 0:
            raise ValueError("Fuel level cannot be negative")

        self.fuel_type = fuel_type
        self.fuel_level = fuel_level

    @property
    def range(self) -> float:
        """Returns the estimated driving range in kilometers."""
        return self.fuel_level / self.FUEL_CONSUMPTION * 100

    def drive(self, km: float) -> None:
        """Consumes fuel and increases mileage if enough fuel is available."""
        if not km > 0:
            raise ValueError("Distance must be greater than 0")

        required_fuel = km * self.FUEL_CONSUMPTION / 100

        if required_fuel > self.fuel_level:
            raise ValueError("Not enough fuel for the trip")

        self.fuel_level -= required_fuel
        super().drive(km)
        print(f"Fuel consumed: {required_fuel:.2f} liters")

    def refuel(self, liters: float) -> None:
        """Adds a positive amount of fuel to the tank."""
        if not liters > 0:
            raise ValueError("Fuel amount must be greater than 0")

        self.fuel_level += liters

    def status(self) -> str:
        """Returns vehicle details, remaining fuel, and driving range."""
        return (
            f"{super().status()}; "
            f"fuel type: {self.fuel_type}; "
            f"fuel level: {self.fuel_level:.2f} liters; "
            f"range: {self.range:.1f} km"
        )


class ElectricCar(Car):
    """Represents an electric car powered by a rechargeable battery."""

    BATTERY_CONSUMPTION: float = 20.0

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        battery_level: float = 100,
    ) -> None:
        """Initializes an electric car with a battery level from 0 to 100%."""
        Vehicle.__init__(self, make, model, year)

        if not 0 <= battery_level <= 100:
            raise ValueError("Battery level must be between 0 and 100%")

        self.battery_level = battery_level

    @property
    def range(self) -> float:
        """Returns the estimated driving range based on battery charge."""
        return self.battery_level / self.BATTERY_CONSUMPTION * 100

    def drive(self, km: float) -> None:
        """Consumes battery charge and increases mileage."""
        if not km > 0:
            raise ValueError("Distance must be greater than 0")

        required_charge = km * self.BATTERY_CONSUMPTION / 100

        if required_charge > self.battery_level:
            raise ValueError("Not enough battery charge for the trip")

        self.battery_level -= required_charge
        Vehicle.drive(self, km)
        print(f"Battery charge consumed: {required_charge:.1f}%")

    def refuel(self, liters: float) -> None:
        """Rejects fuel refilling because electric cars require charging."""
        raise NotImplementedError(
            "Electric cars must be charged using charge()"
        )

    def charge(self, percent: float) -> None:
        """Adds battery percentage points without exceeding 100%."""
        if not percent > 0:
            raise ValueError("Charge amount must be greater than 0")

        if self.battery_level + percent > 100:
            raise ValueError("Battery level cannot exceed 100%")

        self.battery_level += percent

    def status(self) -> str:
        """Returns vehicle details, battery level, and driving range."""
        return (
            f"{Vehicle.status(self)}; "
            f"battery level: {self.battery_level:.1f}%; "
            f"range: {self.range:.1f} km"
        )


class Truck(Vehicle):
    """Represents a truck with a limited cargo capacity."""

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        capacity: float,
    ) -> None:
        """Initializes an empty truck with a positive capacity in kilograms."""
        super().__init__(make, model, year)

        if not capacity > 0:
            raise ValueError("Cargo capacity must be greater than 0")

        self.capacity = capacity
        self.cargo_weight: float = 0

    def load(self, kg: float) -> None:
        """Adds cargo without exceeding the truck's capacity."""
        if not kg > 0:
            raise ValueError("Cargo weight must be greater than 0")

        if self.cargo_weight + kg > self.capacity:
            raise ValueError("Cargo capacity exceeded")

        self.cargo_weight += kg

    def unload(self, kg: float) -> None:
        """Removes cargo without exceeding the currently loaded weight."""
        if not kg > 0:
            raise ValueError("Cargo weight must be greater than 0")

        if kg > self.cargo_weight:
            raise ValueError("Cannot unload more cargo than is currently loaded")

        self.cargo_weight -= kg

    def drive(self, km: float) -> None:
        """Increases mileage and reports cargo transport work in tonne-kilometers."""
        super().drive(km)
        print(
            f"Cargo transported: {self.cargo_weight:g} kg; "
            f"transport work: {self.cargo_weight / 1000 * km:g} t·km"
        )

    def status(self) -> str:
        """Returns vehicle details, current cargo weight, and capacity."""
        return (
            f"{super().status()}; "
            f"cargo: {self.cargo_weight:g}/{self.capacity:g} kg"
        )


class FleetManager:
    """Manages a collection of vehicles and provides fleet statistics."""

    def __init__(self) -> None:
        """Initializes an empty fleet."""
        self._vehicles: list[Vehicle] = []

    @property
    def vehicles(self) -> list[Vehicle]:
        """Returns a shallow copy of the fleet's vehicle list."""
        return self._vehicles.copy()

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Adds a vehicle if it is not already in the fleet."""
        if vehicle in self._vehicles:
            raise ValueError("This vehicle is already in the fleet")

        self._vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle) -> None:
        """Removes a vehicle from the fleet."""
        if vehicle not in self._vehicles:
            raise ValueError("Vehicle not found in the fleet")

        self._vehicles.remove(vehicle)

    def total_mileage(self) -> float:
        """Returns the combined mileage of all vehicles in the fleet."""
        return sum(vehicle.mileage for vehicle in self._vehicles)

    def find_by_make(self, make: str) -> list[Vehicle]:
        """Returns vehicles matching the make, ignoring letter case."""
        return [
            vehicle
            for vehicle in self._vehicles
            if vehicle.make.casefold() == make.casefold()
        ]

    def report(self) -> str:
        """Returns each vehicle's status and the fleet's total mileage."""
        descriptions = "\n".join(
            vehicle.status() for vehicle in self._vehicles
        )

        return (
            f"Vehicle count: {len(self._vehicles)}\n"
            f"{descriptions}\n"
            f"Total mileage: {self.total_mileage():g} km"
        )


def main() -> None:
    car1 = Car("Toyota", "Corolla", 2020, "petrol", 20)
    car2 = Car("Volkswagen", "Golf", 2019, "diesel", 15)

    electric1 = ElectricCar("Tesla", "Model 3", 2023, 80)
    electric2 = ElectricCar("Nissan", "Leaf", 2021, 60)

    truck1 = Truck("Volvo", "FH", 2018, 20000)
    truck2 = Truck("MAN", "TGX", 2022, 18000)

    fleet = FleetManager()

    for vehicle in (car1, car2, electric1, electric2, truck1, truck2):
        fleet.add_vehicle(vehicle)

    car1.refuel(10)
    electric1.charge(10)

    truck1.load(10000)
    truck2.load(6000)
    truck2.unload(1000)

    print("INITIAL STATE")
    print(fleet.report())

    print("\nPOLYMORPHISM: drive(100)")
    for vehicle in fleet.vehicles:
        vehicle.drive(100)

    print("\nSTATE AFTER THE TRIP")
    print(fleet.report())

    print("\nSearch results for Toyota:")
    for vehicle in fleet.find_by_make("toyota"):
        print(vehicle.status())

    print("\nTechnical representation:", repr(car1))

    fleet.remove_vehicle(car2)
    print("\nFleet after removing Volkswagen:")
    print(fleet.report())

    try:
        truck1.load(15000)
    except ValueError as error:
        print("\nLoading error:", error)

    try:
        truck2.unload(10000)
    except ValueError as error:
        print("Unloading error:", error)

    try:
        electric1.refuel(10)
    except NotImplementedError as error:
        print("Refueling error:", error)


if __name__ == "__main__":
    main()