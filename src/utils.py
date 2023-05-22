import json
import operator

from src.vacancy import Vacancy


class ParsingError(Exception):
    """Класс для вывода ошибки"""
    def __str__(self):
        return 'Ошибка получения данных'


class SaveJson:
    """Сохраняет данные по вакансиям в json файл"""
    @staticmethod
    def save_json(class_object):
        objects_list = []
        for i in class_object.get_vacancies():
            objects_list.append(i)

        with open(class_object.keyword.lower() + '.json', 'w', encoding='utf-8') as file:
            json.dump(objects_list, file, indent=2, ensure_ascii=False)


def show_vacancy(class_object):
    """Возвращает список для показа в консоль"""
    with open(class_object.keyword.lower() + '.json', 'r', encoding='utf-8') as file:
        data = sorted(json.load(file), key=operator.itemgetter('salary to', 'salary to'), reverse=False)

    vacancies = [Vacancy(line["name"], line["firm"], line["salary from"],
                         line["salary to"], line["url"], line["area"]) for line in data]

    for x in vacancies:
        print(end=f'{"-" * 100}\n')
        print(x)

    return vacancies


def show_top_vacancy(class_object):
    """Возвращает список top-10 вакансий"""
    with open(class_object.keyword.lower() + '.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    vacancies = [Vacancy(line["name"], line["firm"], line["salary from"],
                         line["salary to"], line["url"], line["area"]) for line in data]

    for x in vacancies[:10]:
        print(end=f'{"-" * 100}\n')
        print(x)
