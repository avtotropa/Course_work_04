# Курсовой проект по ООП “Парсер вакансий”

## Задание:

Напишите программу, которая будет получать информацию о вакансиях с разных платформ в
России, сохранять ее в файл и позволять удобно работать с ней (добавлять, фильтровать, удалять). 


### Что сделано

- Создан абстрактный класс APIData для работы с API сайтов с вакансиями. 
- Реализованы классы APIHeadHunter и APISuperJob, наследующиеся от абстрактного класса APIData, для работы 
с конкретными платформами. Классы подключаются к API и получают вакансии.
- Создан класс Vacancy для работы с вакансиями. Определены атрибуты: название вакансии, название фирмы, зарплата, 
ссылка на вакансию, город. 
- Реализованы методы для добавления вакансий в файл, получения данных из файла по указанным критериям.
- Создан класс для сохранения информации о вакансиях в JSON-файл. 
- Все классы и функции объединены в единую программу.

### Особенности проекта

- Значение "количество вакансий (per_page)" задано равным 10
- Поиск происходит по 10 страницам (задано по умолчанию)

### Как пользоваться программой

- После запуска программы, в главном меню, вводите ключевое слово поиска и нажимете Enter.
- В появившемся меню выбираете сайт, вводите номер под которым он отображен в меню и жмете Enter.
- Выводится количество найденных вакансий по запросу.
- Выбираем сортировку или показ всех найденных вакансий (по убыванию)
- Что бы выйти выбираем соответствующий пункт меню


