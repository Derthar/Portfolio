import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
import os
import math
import time
import shutil
import datetime


class DlgMain(QDialog):
    def __init__(self):
        # variables
        # region
        lenght = 800
        height = 600
        first_row = int(math.trunc(0.075 * height))
        second_row = int(math.trunc(0.2 * height))
        third_row = int(math.trunc(0.3 * height))
        first_column = int(math.trunc(0.1 * lenght))
        between_column = int(math.trunc(0.6 * lenght))
        second_column = int(math.trunc(0.875 * lenght))
        # endregion

        super().__init__()  # parent's __init__
        self.setWindowTitle("Backuper GUI")  # add window title
        self.setFixedSize(lenght, height)  # Main window size

        # set attributes
        self.file_name = None
        self.bdir_path = None
        self.program_interval = None
        self.save_interval = None
        self.validator = QIntValidator()


        # set text-labels
        # region
        self.label_file = QLabel('Выберите необходимый файл:', self)
        self.label_file.move(int(0.4*lenght), int(0.025*height))

        self.label_path = QLabel('Выберите бекап-директорию:', self)
        self.label_path.move(int(0.4*lenght), int(0.15*height))

        self.label_interval = QLabel('Введите интервал удаления файлов(в минутах)', self)
        self.label_interval.move(int(first_column), int(0.26 * height))

        self.label_intsave = QLabel('Введите интервал сохранения файлов(в секундах)', self)
        self.label_intsave.move(int(between_column), int(0.26 * height))
        # endregion

        # set text-lines
        # region
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
        # endregion

        # set buttons
        # region
        self.select_file_btn = QPushButton('Select file', self)
        self.select_file_btn.move(second_column, first_row)
        self.select_file_btn.clicked.connect(self.evt_select_file_btn_clicked)

        self.odir_btn = QPushButton('Select backup dir', self)
        self.odir_btn.move(second_column, second_row)
        self.odir_btn.clicked.connect(self.evt_select_bdir_btn_clicked)

        self.start_btn = QPushButton('Get data', self)
        self.start_btn.move(int(0.3*lenght), int(0.9*height))
        self.start_btn.clicked.connect(self.backuper)

        self.cancel_btn = QPushButton("Exit", self)
        self.cancel_btn.move(int(0.55*lenght), int(0.9*height))
        self.cancel_btn.clicked.connect(self.exit_func)
        # endregion

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
        self.File_Text.setDisabled(True)
        self.Path_Text.setDisabled(True)

    def enabled_elements(self):
        self.File_Text.setDisabled(False)
        self.Path_Text.setDisabled(False)
        self.Interval_Text.setDisabled(False)
        self.Int_Save_Text.setDisabled(False)
        self.select_file_btn.setDisabled(False)
        self.odir_btn.setDisabled(False)

    def check_values(self):
        if self.check_file_name() and self.check_bdir_path() and self.check_program_interval() and self.check_program_int_save():
            self.disable_elements()
            self.console_print('Проверка входных данных прошла успешно. Запуск программы...')
            return True
        self.enabled_elements()
        return False

    def check_file_name(self):
        self.console_print('Проверка входных данных')
        if self.file_name is not None and os.path.exists(self.file_name):
            self.console_print('Проверка параметра 1 прошла успешно')
            return True
        else:
            self.console_print('Введите корректный путь до файла, который надо сохранять')
            self.enabled_elements()
            return False

    def check_bdir_path(self):
        if self.bdir_path is not None and os.path.exists(self.bdir_path):
            self.console_print('Проверка параметра 2 прошла успешно')
            return True
        else:
            self.console_print('Введите корректный путь до папки, в которую надо сохранять')
            self.enabled_elements()
            return False

    def check_program_interval(self):
        self.program_interval = self.Interval_Text.text()
        if self.program_interval is not None:
            try:
                int(self.Interval_Text.text())
            except:
                self.console_print('Введите некорректный интервал сохранения')
                self.enabled_elements()
                return False
            self.console_print('Проверка параметра 3 прошла успешно')
            return True

    def check_program_int_save(self):
        self.save_interval = self.Int_Save_Text.text()
        if self.save_interval is not None:
            try:
                int(self.save_interval)
            except:
                self.console_print('Введите корректный интервал удаления')
                self.enabled_elements()
                return False
            self.console_print('Проверка параметра 4 прошла успешно')
            return True
    def backuper(self):
        def inner():
            if self.check_values():
                self.console_print('Старт бэкапа')
                self.console_print(threading.current_thread().name)
                self.console_print(threading.main_thread().name)
                i = 0
                while i != 5:
                    self.console_print(str(i))
                    i += 1
                    time.sleep(i)
        threading.Thread(target=inner(), name='new').start()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = DlgMain()
    program.show()
    sys.exit(app.exec_())
