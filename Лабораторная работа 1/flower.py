import doctest


class Flower:
    def __init__(self, type: str, watering: float):
        """
        Объект "Стакан"

        :param type: Вид цветочка
        :param watering: Сколько раз в неделю его нужно поливать

        Примеры:
        >>> flower = Flower("Ромашка", 3)
        """
        if not isinstance(watering, (int, float)):
            raise TypeError("Частота поливов должна быть типа int или float")
        if watering <= 0:
            raise ValueError("Пожалейте цветочек...")
        self.watering = watering

        if not isinstance(type, str):
            raise TypeError("Вид цветочка должен быть в формате str")
        if len(type) <= 0:
            raise ValueError("Вид цветка должен быть заполнен")
        self.type = type

    def in_red_book(self) -> bool:
        """
        Функция, которая проверяет находится ли цветок в красной книге

        :return: True/False находится ли цветок в красной книге?

        Примеры:
        >>> flower = Flower("Ромашка", 3)
        >>> flower.in_red_book()
        """
        ...

    def pour_the_flower(self, day: int, month: int, year: int) -> None:
        """
        Полив цветка.
        :param day: Хранит день, когда был полит цветок
        :param day: Хранит месяц, когда был полит цветок
        :param day: Хранит год, когда был полит цветок

        :raise Error: Если формат даты был нарушен, то вызываем ошибку

        Примеры:
        >>> flower = Flower("Ромашка", 3)
        >>> flower.pour_the_flower(3, 11, 2023)
        """
        if not isinstance(day, int):
            raise TypeError("День должен быть типа int")
        if not isinstance(month, int):
            raise TypeError("Месяц должен быть типа int")
        if not isinstance(year, int):
            raise TypeError("Год должен быть типа int")
        ...

    def does_it_need_to_water(self, last_data: str, today: str) -> bool:
        """
        Необходимость полива цветочка.

        :param last_data: Дата последнего полива
        :param today: Сегодняшняя дата
        :raise ValueError: Если с даты последнего полива прошло меньше времени, чем нужно для следующего,
        то возвращается ошибка.

        :return: True/False нужно ли поливать

        Примеры:
        >>> flower = Flower("Ромашка", 3)
        >>> flower.does_it_need_to_water("29.01.2024", "02.02.2024")
        """


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
