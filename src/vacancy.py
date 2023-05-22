class Vacancy:
    """Класс для создания объектов Вакансий"""
    __slots__ = ('name', 'firm', 'salary_from', 'salary_to', 'url', 'area')

    def __init__(self, name, firm, salary_from, salary_to, url, area):
        self.name = name
        self.firm = firm
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.area = area

    def __str__(self):
        return f'Вакансия: {self.name}\n' \
               f'Фирма: {self.firm}\n' \
               f'Зарплата: от - {self.salary_from}, до - {self.salary_to}\n' \
               f'Город: {self.area}\n' \
               f'Эл. адрес: {self.url}\n'
