from art import tprint
import colorama
from typing import List


class Record:
    def __init__(self, identificator: int, first_name: str, family_name: str, last_name='Отчество отсутствует',
                 organisation='Не указано', work_phone='Не указан', personal_phone='Не указан') -> None:
        self.id: int = identificator
        self.first_name: str = first_name
        self.family_name: str = family_name
        if last_name:
            self.last_name: str = last_name
        else:
            self.last_name: str = 'Отчество отсутствует'
        if organisation:
            self.organisation: str = organisation
        else:
            self.organisation: str = 'Не указано'
        if work_phone:
            self.work_phone: str = work_phone
        else:
            self.work_phone: str = 'Не указан'
        if personal_phone:
            self.personal_phone: str = personal_phone
        else:
            self.personal_phone: str = 'Не указан'

    """ Строковое представление записи для отображения """
    def __str__(self) -> str:
        return f'Запись номер {self.id}: {self.family_name} {self.first_name} {self.last_name}, ' \
               f'название организации - {self.organisation}, ' \
               f'рабочий телефон - {self.work_phone}, личный телефон - {self.personal_phone}'


class RecordList:
    def __init__(self) -> None:
        self.stack: list = []
        self.number_of_records: int = 0

    '''Заполнение списка данными из текстового файла( осуществляется при старте программы)'''
    def complete_list(self, data: List[list], db) -> None:
        data_sr: list = [db.serializer(item) for item in data]
        for item, item_sr in zip(data, data_sr):
            self.stack.append(Record(**item_sr))
            self.number_of_records += 1

    '''Добавление записи в список'''
    def add(self, data: dict) -> None:
        self.stack.append(Record(**data))
        self.number_of_records += 1
        print(colorama.Fore.GREEN, f'Элемент успешно добавлен : {self.stack[-1].__str__()} \n')

    '''Построчная печать всех записей'''
    def print_records(self) -> None:
        if not self.number_of_records:
            print(colorama.Fore.LIGHTYELLOW_EX, 'В справочнике еще нет записей')
        for record in self.stack:
            print(colorama.Fore.YELLOW, record.__str__())
        print(colorama.Fore.GREEN, f'Вывод {self.number_of_records} записей завершен\n')

    '''Поиск записи по номеру'''
    def search_record_by_number(self, value: int) -> Record:
        if not self.number_of_records:
            print(colorama.Fore.RED, 'В базе данных пока нет записей :(')
        elif value > self.number_of_records:
            print(colorama.Fore.RED, 'Такой записи не существует')
        else:
            for record in self.stack:
                if record.id == value:
                    return record

    '''Поиск записи/записей по текстовому полю'''
    def search_records_by_value(self, value: str, many=False) -> None:
        """ обработка крайнего случая """
        if not self.number_of_records:
            print(colorama.Fore.RED, 'В базе данных пока нет записей :(')
            return

        """ Поиск всех подходящих записей """
        if many:
            flag: bool = False
            for record in self.stack:
                if value in record.__str__().lower():
                    print(colorama.Fore.LIGHTYELLOW_EX, record.__str__())
                    flag: bool = True
            if not flag:
                print(colorama.Fore.RED, 'К сожалению таких записей не нашлось...')

        # Поиск первой попавшейся записи
        else:
            flag: bool = False
            for record in self.stack:
                if value in record.__str__().lower():
                    print(colorama.Fore.LIGHTYELLOW_EX, record.__str__())
                    flag += True
                    return
            if not flag:
                print(colorama.Fore.RED, 'К сожалению такая запись не нашлось...')

    '''Поиск записи/записей по нескольким текстовым полям'''
    def search_records_by_values(self, fields: List, full=False, many=False) -> None:

        """ обработка крайнего случая """
        if not self.number_of_records:
            print(colorama.Fore.RED, 'В базе данных пока нет записей :(')

        # Поиск первой подходящей записи
        elif not many:

            '''Поиск по совпадению всех полей'''
            if full:
                for record in self.stack:
                    flag = True
                    for value in fields:
                        if value not in record.__str__().lower():
                            flag *= False
                    if flag:
                        print(colorama.Fore.LIGHTYELLOW_EX, record.__str__())
                        return
                print(colorama.Fore.RED, 'К сожалению таких записей не нашлось...')

            # Поиск по совпадению хотя-бы одного поля'''
            else:
                for record in self.stack:
                    for value in fields:
                        if value in record.__str__().lower():
                            print(colorama.Fore.LIGHTYELLOW_EX, record.__str__())
                            return
                print(colorama.Fore.RED, 'К сожалению таких записей не нашлось...')

        # Поиск всех подходящих записей'''
        else:

            '''Поиск по совпадению всех полей'''
            if full:
                counter: bool = False
                for record in self.stack:
                    flag: bool = True
                    for value in fields:
                        if value not in record.__str__().lower():
                            flag *= False
                    if flag:
                        print(colorama.Fore.LIGHTYELLOW_EX, record.__str__())
                        counter += True
                if not counter:
                    print(colorama.Fore.RED, 'К сожалению таких записей не нашлось...')

            # Поиск по совпадению хотя-бы одного поля'''
            else:
                flag: bool = False
                for record in self.stack:
                    for value in fields:
                        if value in record.__str__().lower():
                            print(colorama.Fore.LIGHTYELLOW_EX, record.__str__())
                            flag += True
                            break
                if not flag:
                    print(colorama.Fore.RED, 'К сожалению таких записей не нашлось...')

    '''Изменение записи'''
    def change_record(self, number: int, data: dict) -> str:
        self.stack[number-1] = Record(**data)
        return 'Запись успешно изменена'


class DBWorker:

    def __init__(self) -> None:
        self.data = []

    '''Выборка данных из текстового файла, заполнение стека и списка невалидных строк'''
    def get_data(self) -> List[list]:
        with open('DataBase.txt', 'r') as file:
            n: int = 0
            error_list: str = ''
            for line in file:
                n += 1
                items = [item.strip() for item in line.split(';')]
                if self.validate_row(items):
                    self.data.append(items)
                else:
                    error_list = error_list + f'{n}, '
            if error_list:
                print(colorama.Fore.RED, f'В некоторых строках имеются некорректные данные: {error_list}')
        return self.data

    '''ДОбавление новой записи в текстовый файл'''
    def write_data(self, data: list) -> None:
        with open('DataBase.txt', 'a') as file:
            file.write(self.deserealizer(data))

    ''' Перезапись имеющейся строки '''
    def rewrite_data(self, number: int, data: List) -> None:
        with open('DataBase.txt', 'r') as file:
            text: str = file.read()
        old_row: str = text.split('\n')[number-1]
        new_row: str = self.deserealizer(data).replace('\n', '')
        with open('DataBase.txt', 'w') as file:
            file.write(text.replace(old_row, new_row))

    '''Проверка корректности данных в строке данных'''
    @staticmethod
    def validate_row(row: List) -> bool:

        # Проверка количества аргументов
        if len(row) != 7:
            return False

        # Проверка присутствия хотя-бы одного номера телефона
        if len(row[5]) == 0 and len(row[6]) == 0:
            return False

        # Проверка, являются ли текстовые поля текстовыми
        for item in row[1:4]:
            if len(item) != 0 and not item.isalpha():
                return False

        # Проверка являются ли числовые поля числовыми
        try:
            int(row[0])
            row[6] = row[6].replace('-', '')
            if len(row[6]) != 0:
                if row[6].startswith('+'):
                    int(row[6][1:])
                else:
                    int(row[6])
            if len(row[5]) != 0:
                if row[5].startswith('+'):
                    int(row[5][1:])
                else:
                    int(row[5])
        except Exception as ex:
            print(ex)
            return False
        return True

    '''Создание словаря для передачи в класс Record'''
    @staticmethod
    def serializer(items: List) -> dict:
        return {
            'identificator': int(items[0]),
            'first_name': items[1],
            'family_name': items[2],
            'last_name': items[3],
            'organisation': items[4],
            'work_phone': items[5],
            'personal_phone': items[6]
        }

    '''Создание строки для записи в текстовый файл'''
    @staticmethod
    def deserealizer(items: List) -> str:
        return f'\n{items[0]};{items[1]};{items[2]};{items[3]};{items[4]};{items[5]};{items[6]}'


def data_input(number: int) -> list:
    dt = [number]
    print(colorama.Fore.CYAN, 'Введите имя (цифры и символы недопустимы)')
    dt.append(input())
    print(colorama.Fore.CYAN, 'Введите фамилию (цифры и символы недопустимы)')
    dt.append(input())
    print(colorama.Fore.CYAN, 'Введите отчество (цифры и символы недопустимы)\n'
                              'Если отчество отсутсвует - нажмите Enter')
    dt.append(input())
    print(colorama.Fore.CYAN, 'Введите организацию (цифры и символы недопустимы)\n'
                              'Если организация неизвестна - нажмите Enter')
    dt.append(input())
    print(colorama.Fore.CYAN, 'Введите рабочий телефон (цифры и символы недопустимы)\n'
                              'Если номер телефона неизвестен - нажмите Enter. '
                              'Для занесение в справочник должен\n'
                              'быть известен хотя-бы один номер телефона')
    dt.append(input())
    print(colorama.Fore.CYAN, 'Введите личный телефон (цифры и символы недопустимы)\n'
                              'Если номер телефона неизвестен - нажмите Enter. Но для занесение '
                              'в справочник должен быть известен хотя-бы один номер телефона')
    dt.append(input())
    return dt


def main():

    """Инициализация классов и первое прочтение текстового файла"""
    colorama.init()
    print(colorama.Fore.LIGHTBLUE_EX, '')
    tprint('Phonebook')
    database = DBWorker()
    lst = RecordList()
    lst.complete_list(data=database.get_data(), db=database)
    flag: bool = True

    ''' Консольное меню '''
    while flag:
        print(colorama.Fore.LIGHTBLUE_EX, 'Выберите необходимую опцию: \n1: Печатать список всех записей \n'
                                          '2: Добавить запись \n3: Найти запись \n'
                                          '4: Изменить запись \n9: Выход')
        a1: str = input()

        match a1:

            # Выбор печати всех элементов
            case '1':
                lst.print_records()

            # Выбор добавления нового элемента
            case '2':
                while True:
                    number: int = lst.stack[-1].id + 1
                    data: list = data_input(number=number)
                    if database.validate_row(data):
                        lst.add(data=database.serializer(data))
                        database.write_data(data)
                        break
                    else:
                        print(colorama.Fore.CYAN,
                              'К сожaлению данные не прошли проверку, возможно вы где-то ошиблись.\n'
                              'Попробуете еще раз? [Y/N]')
                        inp: str = input()
                        match inp.lower().strip():

                            case 'y':
                                continue

                            case 'n':
                                return

            # Выбор поиска
            case '3':
                print(colorama.Fore.LIGHTBLUE_EX, 'Выберите необходимую опцию: \n1: по номеру записи\n'
                                                  '2: по другому полю\n3: по нескольким полям')
                a2: str = input()
                match a2:

                    # Поиск по номеру записи
                    case '1':
                        print(colorama.Fore.LIGHTBLUE_EX, 'Введите номер записи')
                        a3: int = int(input())
                        print(colorama.Fore.LIGHTYELLOW_EX,
                              lst.search_record_by_number(value=a3).__str__())

                    # Поиск по текстовому полю
                    case '2':
                        print(colorama.Fore.LIGHTBLUE_EX, 'Выберите необходимую опцию: \n1: Поиск одного элемента\n'
                                                          '2: Поиск нескольких элементов')
                        a3: str = input()
                        print(colorama.Fore.LIGHTBLUE_EX,
                              'Введите значение поля')
                        field: str = input().lower()
                        match a3:

                            # Поиск первого совпавшего элемента
                            case '1':
                                lst.search_records_by_value(value=field, many=False)

                            # Поиск всех совпавших элементов
                            case '2':
                                lst.search_records_by_value(value=field, many=True)

                    # Поиск по нескольким текстовым полям
                    case '3':
                        print(colorama.Fore.LIGHTBLUE_EX, 'Выберите необходимую опцию: \n1: Поиск одного элемента\n'
                                                          '2: Поиск нескольких элементов')
                        a3: str = input()
                        print(colorama.Fore.LIGHTBLUE_EX, 'Введите все известные поля через пробел')
                        fields: list = [item.lower() for item in input().split(' ')]
                        print(colorama.Fore.LIGHTBLUE_EX, 'Выберите необходимую опцию: \n'
                                                          '1: Поиск по полному вхождению всех полей\n'
                                                          '2: Поиск по вхождению любого поля')
                        a4: str = input()
                        match a3:

                            # Поиск первого совпавшего элемента
                            case '1':
                                match a4:

                                    # Поиск по полному вхождению всех полей
                                    case '1':
                                        lst.search_records_by_values(fields=fields, full=True)

                                    # Поиск по вхождению хотя бы одного поля
                                    case '2':
                                        lst.search_records_by_values(fields=fields, full=False)

                            # Поиск всех совпавших элементов
                            case '2':
                                match a4:

                                    # Поиск по полному вхождению всех полей
                                    case '1':
                                        lst.search_records_by_values(fields=fields, full=True)

                                    # Поиск по вхождению хотя бы одного поля
                                    case '2':
                                        lst.search_records_by_values(fields=fields, full=False)

            # Выбор изменения записи
            case '4':
                print(colorama.Fore.LIGHTBLUE_EX, 'Введите номер записи')
                a2: int = int(input())
                if a2 > lst.number_of_records:
                    print(colorama.Fore.RED, 'Такой записи не существует')
                    continue
                data: list = data_input(number=a2)
                lst.change_record(number=a2, data=database.serializer(data))
                database.rewrite_data(number=a2, data=data)

            # Завершение работы программы
            case '9':
                tprint('Have a good day!')
                flag = False


if __name__ == '__main__':
    main()
