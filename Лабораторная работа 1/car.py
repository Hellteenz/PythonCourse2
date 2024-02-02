import doctest


class Car:
    def __init__(self, fuel_level: float, license_plate: int):
        """
        Объект "Машина"

        :param fuel_level: топливный запас
        :param license_plate: номерной знак в формате одних только цифр

        Примеры:
        >>> car = Car(60, 123456)
        """
        if not isinstance(license_plate, int):
            raise TypeError("Номерной знак должен быть типа int")
        if license_plate <= 0:
            raise ValueError("Номерной знак должен быть положительным числом")
        self.license_plate = license_plate

        if not isinstance(fuel_level, (int, float)):
            raise TypeError("Топливный запас должен быть типа int или float")
        if fuel_level < 0:
            raise ValueError("Топливный запас должен быть неотрицательным числом")
        self.fuel_level = fuel_level

    def need_more_fuel(self) -> bool:
        """
        Функция, которая подсказывает пользователю нужно ли заправить машину

        :return: True/False нужно ли заправлять?

        Примеры:
        >>> car = Car(60, 123456)
        >>> car.need_more_fuel()
        """

    def is_car_in_search(self, police_data: list) -> bool:
        """
        Поиск машины в полицейской базе розыска.
        :param police_data: Список с номерными знаками

        :raise ValueError: Если номер из списка задан не числом, то вызываем ошибку

        :return: True/False в розыске ли машина?

        Примеры:
        >>> car = Car(60, 123456)
        >>> car.is_car_in_search([123, 99273, 726452])
        """
        for i in range(len(police_data)):
            if int(police_data[i]) is None:
                raise ValueError("Номерные знаки должны задаваться числом")

    def filling(self, num_max_fuel: dict, add: float) -> None:
        """
        Заправка

        :param num_max_fuel: Словарь, где ключ - первая цифра номерного знака,
        значение - соответствующий объем бака
        :raise ValueError: Если добавить хотят больше, чем вмещает бак, то возвращается ошибка.

        :return: Пополнение бака

        Примеры:
        >>> car = Car(60, 123456)
        >>> car.filling({1: 80, 2: 60, 7: 50, 9: 90}, 15)
        """



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
