import doctest


class Student:
    def __init__(self, grade: int, aver_mark: float):
        """
        Объект "Студент"

        :param grade: Курс обучения
        :param aver_mark: Средний балл

        Примеры:
        >>> student = Student(2, 4.6)
        """
        if not isinstance(grade, int):
            raise TypeError("Курс обучения должен быть типа int")
        if grade <= 0:
            raise ValueError("Вы еще не студент?")
        self.grade = grade

        if not isinstance(aver_mark, (int, float)):
            raise TypeError("Средний балл должен быть типа int или float")
        if aver_mark < 2:
            raise ValueError("Вы уже не студент...")
        if aver_mark > 5:
            raise ValueError("Неверно введены данные")
        self.aver_mark = aver_mark

    def the_probability_of_repass(self) -> bool:
        """
        Функция, которая высчитывает вероятность нахождения студента на дополнительной сессии в
        зависимости от среднего балла

        :return: True, если есть вероятность, False, если нет

        Примеры:
        >>> student = Student(2, 4.6)
        >>> student.the_probability_of_repass()
        """

    def will_he_be_transferred(self, passing_mark: float) -> bool:
        """
        Перевод на следующий курс.
        :param passing_mark: Проходной балл для перевода на следующий курс

        :raise ValueError: Если проходной балл больше 5 или меньше 2, то вызываем ошибку

        :return: True/False, переведут или нет.

        Примеры:
        >>> student = Student(2, 4.6)
        >>> student.will_he_be_transferred(4.8)
        """
        if not isinstance(passing_mark, (int, float)):
            raise TypeError("Проходной балл должен быть типа int или float")
        if not 2.0 < passing_mark <= 5.0:
            raise ValueError("Средний балл должен быть в диапазоне от 2х до 5ти")

    def change_aver_mark(self, new_mark: int) -> None:
        """
        Изменение среднего балла

        :param new_mark: Новая оценка
        :raise ValueError: Если оценка больше 5 или меньше 2, то возвращается ошибка.

        :return: Обновленный средний балл

        Примеры:
        >>> student = Student(2, 4.6)
        >>> student.will_he_be_transferred(5)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
