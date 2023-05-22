from src.classes_api import APIHeadHunter, APISuperJob

from src.utils import SaveJson, show_vacancy, show_top_vacancy


def main():
    while True:
        print(end=f'{"-" * 100}\n')
        print('ПРОГРММА ДЛЯ ПОИСКА ВАКАНСИЙ.\nГлавное меню')
        print(end=f'{"-" * 100}\n')
        user_input_vac = input('Введите ключевое слово поиска: ').title()
        print(end=f'{"-" * 100}\n')
        print('Выберите сайт. Наберите номер и нажмите Enter:\n1 - Head Hunter\n2 - Super Job\n3 - Выход')
        user_choice_platform = input()

        if user_choice_platform == '1':
            print('Вы выбрали сайт - Head Hunter')
            print(end=f'{"-" * 100}\n')
            hh = APIHeadHunter(user_input_vac)
            SaveJson.save_json(hh)
            while True:
                print('Выберите действие:\n1 - Показать все вакансии\n2 - Показать ТОП-10 вакансий\n'
                      '3 - В главное меню\n4 - Выход')
                user_choice = input()
                if user_choice == '1':
                    show_vacancy(hh)
                elif user_choice == '2':
                    show_top_vacancy(hh)
                elif user_choice == '3':
                    break
                else:
                    print(end=f'{"-" * 100}\n')
                    print('До новых встреч! Успешных собеседований!')
                    exit()

        if user_choice_platform == '2':
            print('Вы выбрали сайт - Super Job')
            print(end=f'{"-" * 100}\n')
            sj = APISuperJob(user_input_vac)
            SaveJson.save_json(sj)
            while True:
                print('Выберите действие:\n1 - Показать все вакансии\n2 - Показать ТОП-10 вакансий\n'
                      '3 - В главное меню\n4 - Выход')
                user_choice = input()
                if user_choice == '1':
                    show_vacancy(sj)
                elif user_choice == '2':
                    show_top_vacancy(sj)
                elif user_choice == '3':
                    break
                else:
                    print(end=f'{"-" * 100}\n')
                    print('До новых встреч! Успешных собеседований!')
                    exit()

        if user_choice_platform == '3':
            exit()

if __name__ == '__main__':
    main()
