from typing import List


class Trip:
    def __init__(self, distance:float, comment: str = "Просто поездка") -> None:
        self.distance = distance
        self.comment = comment


class Transport:
    def __init__(self, fuel:int, trips: List[Trip]) -> None:
        self.fuel = fuel
        self.trips = trips

    def add_trips(self, trip: Trip) -> None:
        """Добавляет поездку."""
        
        self.trips.append(trip)

    def sum_trip_distance(self) -> float:
        """Рассчитает всю пройденную дистанцию данного вида транспорта."""

        return sum([trip.distance for trip in self.trips])

    def calc_reachable_distance(self):
        """Рассчитывает оставшийся путь трансортного средства с учетом совершенных поездок."""
        raise NotImplementedError("Для базового класса нет реализации метода.")
        


class Car(Transport):
    FUEL_CONSUMPTION_CAR = 0.12 # л/км
    
    def calc_reachable_distance(self) -> str:
        """Рассчитывает оставшийся путь автомобиля с учетом совершенных поездок."""
        result = (self.fuel - self.sum_trip_distance() * self.FUEL_CONSUMPTION_CAR) // self.FUEL_CONSUMPTION_CAR
        return f'Машине осталость ехать {result} км.'


class Airplane(Transport):
    FUEL_CONSUMPTION_AIRPLANE = 200

    def calc_reachable_distance(self) -> str:
        """Рассчитывает оставшееся время полета с учетом совершенных поездок."""
        result = (self.fuel - self.sum_trip_distance() * self.FUEL_CONSUMPTION_AIRPLANE) // self.FUEL_CONSUMPTION_AIRPLANE
        return f'Самолету осталось летать {result}'


audi = Car(70, [
    Trip(200, "Калуга-Москва"),
    Trip(50, "В лес")
])

print(audi.calc_reachable_distance())