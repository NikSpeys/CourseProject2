class WorkVacancy:
    """Класс работы с вакансиями и сравнение зарплат"""

    __slots__ = ('__name', '__description', '__salary', '__link', '__area')

    def __init__(self, vacancy):
        self.__name = vacancy['name'] if vacancy['name'] else 'Название не указано'
        self.__description = vacancy['snippet']["responsibility"] if vacancy['snippet'] and vacancy['snippet'][
            "responsibility"] else 'Описание отсутствует'
        self.__salary = vacancy['salary']['from'] if vacancy['salary'] and vacancy['salary']['from'] else 0
        self.__link = vacancy['alternate_url'] if vacancy['alternate_url'] else 'Ссылка не указана'
        self.__area = vacancy['area']['name'] if vacancy['area'] and vacancy['area']['name'] else 'Город не указан'

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def salary(self):
        return self.__salary

    @property
    def link(self):
        return self.__link

    @property
    def area(self):
        return self.__area

    def __str__(self):
        return (
            f'Вакансия: {self.name}, '
            f'Описание: {self.description}, '
            f'Зарплата: {self.salary}, '
            f'Ссылка: {self.link}, '
            f'Город: {self.area}'
        )

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __lt__(self, other):
        return self.salary < other.salary


if __name__ == '__main__':  # pragma: no cover
    vacancy_1 = {
        'name': 'nik',
        'salary': None,
        'alternate_url': None,
        'snippet': None,
        'area': None
    }

    x = WorkVacancy(vacancy_1)
    print(x)
