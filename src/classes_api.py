import os

import requests
import operator
from abc import ABC, abstractmethod

from src.utils import ParsingError

USD = 78  # курс доллара
PER_PAGE = 10  # количество вакансий на странице


class APIData(ABC):
    """Абстрактный класс для получения данных по API"""

    @abstractmethod
    def get_vacancies(self):
        pass


class APIHeadHunter(APIData):
    """Класс для обработки полученных данных по вакансиям с Head Hunter"""

    def __init__(self, keyword):
        self.keyword = keyword
        self.__page: int = 0
        self.__per_page: int = PER_PAGE

    def get_vacancies(self):
        """Метод получения данных. Возвращает список отсортированный по убыванию"""

        vacancies = []

        while self.__page < 10:

            response = requests.get(url='https://api.hh.ru/vacancies',
                                    headers={'User-Agent': 'MyApp / 1.0(my - app - feedback @ example.com)'},
                                    params={'text': self.keyword, 'area': '113',
                                            'page': self.__page, 'per_page': self.__per_page})
            if response.status_code != 200:
                raise ParsingError

            for row in response.json()['items']:
                if row['salary'] is not None:
                    self.get_salary(row)
                    vacancies.append({
                        'name': row['name'],
                        'firm': row['employer']['name'],
                        'salary from': row['salary']['from'],
                        'salary to': row['salary']['to'],
                        'url': row['alternate_url'],
                        'area': row['area']['name'],
                    })
            self.__page += 1
        print(f"Найдено {len(vacancies)} вакансий.")
        return sorted(vacancies, key=operator.itemgetter('salary to', 'salary to'), reverse=True)

    @staticmethod
    def get_salary(sal: dict):
        """Метод для учета курса доллара"""
        sal['salary']['from'] = 0 if sal['salary']['from'] is None else sal['salary']['from']
        sal['salary']['to'] = 0 if sal['salary']['to'] is None else sal['salary']['to']
        if sal['salary']['currency'].lower() == 'usd':
            sal['salary']['from'] = sal['salary']['from'] * USD
            sal['salary']['to'] = sal['salary']['to'] * USD


class APISuperJob(APIData):
    """Класс для обработки полученных данных по вакансиям с SuperJob"""

    def __init__(self, keyword):
        self.keyword = keyword
        self.__page: int = 0
        self.__per_page: int = PER_PAGE

    def get_vacancies(self):
        """Метод получения данных. Возвращает список отсортированный по убыванию"""

        vacancies = []

        while self.__page < 10:

            response = requests.get(url='https://api.superjob.ru/2.0/vacancies',
                                    headers={'X-Api-App-Id': os.getenv('SuperJob_API')},
                                    params={'keyword': self.keyword, 'page': self.__page, 'count': self.__per_page})
            if response.status_code != 200:
                raise ParsingError

            for row in response.json()['objects']:
                self.get_salary(row)
                vacancies.append({
                    'name': row['profession'],
                    'firm': row['firm_name'],
                    'salary from': row['payment_from'],
                    'salary to': row['payment_to'],
                    'url': row['link'],
                    'area': row['town']['title'],
                })
            self.__page += 1
        print(f"Найдено {len(vacancies)} вакансий.")
        return sorted(vacancies, key=operator.itemgetter('salary to', 'salary to'), reverse=True)

    @staticmethod
    def get_salary(sal: dict):
        sal['payment_from'] = 0 if sal['payment_from'] is None else sal['payment_from']
        sal['payment_to'] = 0 if sal['payment_to'] is None else sal['payment_to']
        if sal['currency'].lower() == 'usd':
            sal['payment_from'] = sal['payment_from'] * USD
            sal['payment_to'] = sal['payment_to'] * USD
