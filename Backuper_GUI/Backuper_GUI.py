import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QThread
import os
import math
import time
import shutil
import datetime
from threading import Thread


class DlgMain(QDialog):
    def __init__(self):
        global th
        lenght = 800
        height = 600
        first_row = int(math.trunc(0.075 * height))
        second_row = int(math.trunc(0.2 * height))
        third_row = int(math.trunc(0.3 * height))
        first_column = int(math.trunc(0.1 * lenght))
        between_column = int(math.trunc(0.6 * lenght))
        second_column = int(math.trunc(0.875 * lenght))
        super().__init__()  # parent's __init__
        self.setWindowTitle("Backuper GUI")  # add window title
        self.setFixedSize(lenght, height)  # Main window size
        self.th = EndlessCycle()

        # set attributes
        self.file_name = ''
        self.bdir_path = ''
        self.validator = QIntValidator()

        # set text-labels
        self.label_file = QLabel('Выберите необходимый файл:', self)
        self.label_file.move(int(0.4*lenght), int(0.025*height))

        self.label_path = QLabel('Выберите бекап-директорию:', self)
        self.label_path.move(int(0.4*lenght), int(0.15*height))

        self.label_interval = QLabel('Введите интервал удаления файлов(в минутах)', self)
        self.label_interval.move(int(first_column), int(0.26 * height))

        self.label_intsave = QLabel('Введите интервал сохранения файлов(в секундах)', self)
        self.label_intsave.move(int(between_column), int(0.26 * height))

        # set text-lines
        self.File_Text = QLineEdit('', self)  # add text line
        self.File_Text.move(first_column, first_row)  # move text line
        self.File_Text.setFixedSize(int(0.725*lenght), int(0.035*height))

        self.Path_Text = QLineEdit('', self)  # add text line
        self.Path_Text.move(first_column, second_row)  # move text line
        self.Path_Text.setFixedSize(int(0.725*lenght), int(0.035*height))

        self.Interval_Text = QLineEdit('10', self)  # add text line
        self.Interval_Text.move(first_column, third_row)  # move text line
        self.Interval_Text.setFixedSize(int(0.2*lenght), int(0.035*height))
        self.Interval_Text.setValidator(self.validator)

        self.Int_Save_Text = QLineEdit('60', self)  # add text line
        self.Int_Save_Text.move(between_column, third_row)  # move text line
        self.Int_Save_Text.setFixedSize(int(0.2*lenght), int(0.035*height))
        self.Int_Save_Text.setValidator(self.validator)

        self.terminal = QTextEdit('', self)
        self.terminal.move(int(0.1*lenght), int(0.4*height))
        self.terminal.setFixedSize(int(0.725*lenght), int(0.45*height))
        self.terminal.setReadOnly(True)

        # set buttons
        self.select_file_btn = QPushButton('Select file', self)
        self.select_file_btn.move(second_column, first_row)
        self.select_file_btn.clicked.connect(self.evt_select_file_btn_clicked)

        self.odir_btn = QPushButton('Select backup dir', self)
        self.odir_btn.move(second_column, second_row)
        self.odir_btn.clicked.connect(self.evt_select_bdir_btn_clicked)

        self.start_btn = QPushButton('Get data', self)
        self.start_btn.move(int(0.3*lenght), int(0.9*height))
        self.start_btn.clicked.connect(self.th.start)  # backuper)

        self.cancel_btn = QPushButton("Cancel", self)
        self.cancel_btn.move(int(0.55*lenght), int(0.9*height))
        self.cancel_btn.clicked.connect(self.exit_func)

        self.console_print('Инициализация прошла успешно. Приложение готово к работе!')

    def evt_select_file_btn_clicked(self):
        select_file, s_ok = QFileDialog.getOpenFileName(self, 'Select File', os. getcwd())
        if s_ok:
            self.File_Text.setText(select_file)
            self.File_Text.setDisabled(True)
            self.file_name = select_file

    def evt_select_bdir_btn_clicked(self):
        p_dir = QFileDialog.getExistingDirectory()
        if p_dir:
            self.Path_Text.setText(p_dir)
            self.Path_Text.setDisabled(True)
            self.bdir_path = p_dir

    @staticmethod
    def exit_func():
        sys.exit()

    def console_print(self, text):
        self.terminal.append(text)

    def disable_elements(self):
        self.Interval_Text.setDisabled(True)
        self.Int_Save_Text.setDisabled(True)
        self.select_file_btn.setDisabled(True)
        self.odir_btn.setDisabled(True)

    def enabled_elements(self):
        self.File_Text.setDisabled(False)
        self.Path_Text.setDisabled(False)
        self.Interval_Text.setDisabled(False)
        self.Int_Save_Text.setDisabled(False)
        self.select_file_btn.setDisabled(False)
        self.odir_btn.setDisabled(False)

class EndlessCycle(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            c=0
            program.console_print('c')
            c+=1


def check_values():
    global program
    if check_file_name() is True and check_bdir_path() is True:
        program.disable_elements()
        program.console_print('Проверка входных данных прошла успешно. Запуск программы...')


def check_file_name():
    program.console_print('Проверка входных данных')
    if program.file_name is not None and os.path.exists(program.file_name):
        program.console_print('Проверка параметра 1 прошла успешно')
        return True
    else:
        program.console_print('Введите корректный путь до файла, который надо сохранять')
        program.enabled_elements()
        return False


def check_bdir_path():
    if program.bdir_path is not None and os.path.exists(program.bdir_path):
        program.console_print('Проверка параметра 2 прошла успешно')
        return True
    else:
        program.console_print('Введите корректный путь до папки, в которую надо сохранять')
        program.enabled_elements()
        return False


# def check_program_interval():
#     if program.interval is not None:
#         try:
#             int(program.interval)
#             program.console_print('Проверка параметра 3 прошла успешно')
#         except:
#             program.console_print('Введите некорректный интервал сохранения')
#             program.enabled_elements()
#             return False
#         return True
#
#
# def check_program_int_save():
#     if program.interval is not None:
#         try:
#             int(program.int_save)
#             program.console_print('Проверка параметра 4 прошла успешно')
#         except:
#             program.console_print('Введите корректный интервал удаления')
#             program.enabled_elements()
#             return False
#         return True


def backuper():
    global program
    program.disable_elements()
    program.interval = float(program.Interval_Text.text())
    program.int_save = program.Int_Save_Text.text()
    check_values()
    delta_interval = datetime.timedelta(minutes=program.interval)
    time_interval = datetime.datetime.strptime(f'{str(delta_interval)}', '%H:%M:%S')

    file_type = ''
    try:
        file_name_str = program.file_name.split('/')[-1]
        file_pure_name = file_name_str.split('.')[0]
        file_type = '.' + file_name_str.split('.')[1]
    except:
        program.console_print('Используется файл без расширения')
        file_pure_name = program.file_name.split('/')[-1]
    program.console_print(file_name_str)
    program.console_print(file_pure_name)
    program.console_print(file_type)
    parent_path = program.file_name.replace(program.file_name.split('/')[-1], '')
    program.console_print(parent_path)
    files_name = []
    files_date = []
    files_time = []
    program.console_print('4')
    # c=0
    # #while True:
    # for c in range(10):
    #     program.console_print(f'Попытка {c}')
    #     c+=1
    #     time.sleep(10)
        # moment = datetime.datetime.now()
        # program.console_print(moment)
        # time.sleep(program.int_save)
        # Определение текущей даты-времени
        # moment_divided = str(moment).split(' ')												# Отделить текущую дату от времени
        # time_divided = moment_divided[1].split('.')											# отсечение миллисекунд от времени
        # moment_date = datetime.datetime.strptime(f'{str(moment_divided[0])}', '%Y-%m-%d')  	# запись текущей даты
        # moment_time = datetime.datetime.strptime(f"{str(time_divided[0])}", '%H:%M:%S')		# запись текущего времени
        # time_record = str(moment_time).replace(':', ' ')
        # time_for_record = time_record.split(' ')
        # try:
        #     new_file_name = (f'{file_pure_name} {moment_date.date()} {time_for_record[1]}-{time_for_record[2]}-{time_for_record[3]}{file_type}').strip()
        #     shutil.copy(f"{parent_path}/{program.file_name.split('/')[-1]}", f"{program.bdir_path}/{new_file_name}")
        #     program.console_print(f"Сохранение файла {new_file_name}")
        # except Exception:
        #     program.console_print('Файл недоступен в данный момент')
        #     time.sleep(program.int_save)
        #     continue
        # Заполнение импровизированной БД
        # files_name.append(new_file_name)
        # files_date.append(moment_date)
        # files_time.append(moment_time)
        # lenght=len(files_name)
    #
    # #Проверка по "БД"
    #     for i in range(lenght):
    #         if moment_date!=files_date[i-1]:
    #             files_date.pop(i-1)
    #             files_time.pop(i-1)
    #             try:
    #                 os.remove(f"{program.bdir_path}/{files_name[i - 1]}")
    #                 program.console_print(f"Удаление файла {files_name[i - 1]}")
    #             except Exception as program:
    #                 program.console_print('Файл уже не существует')
    #             files_name.pop(i-1)
    #         else:
    #             crutch=(moment_time-time_interval)
    #             crutch2=datetime.datetime.strptime(f"{str(crutch)}",'%H:%M:%S')
    #             if crutch2>files_time[i-1]:
    #                 files_date.pop(i-1)
    #                 files_time.pop(i-1)
    #                 try:
    #                     os.remove(f"{program.bdir_path}/{files_name[i - 1]}")
    #                     program.console_print(f"Удаление файла {files_name[i - 1]}")
    #                 except Exception as program:
    #                     program.console_print('Файл уже не существует')
    #                 files_name.pop(i-1)
    #
        #time.sleep(program.int_save)

    # ex.console_print('Вроде получилось')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = DlgMain()
    program.show()
    th = EndlessCycle()
    sys.exit(app.exec_())