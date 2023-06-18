import os
import time
from PyQt5.QtWidgets import *
import sys
import win32serviceutil
from PyQt5.QtGui import QIcon
import threading
# pyinstaller --onefile -w --icon=2.ico read_logs.py


class DlgMain(QDialog):
    def __init__(self):
        # set variables
        # region
        self.window_width = 700
        self.window_height = 500
        self.column1 = int(0.05*self.window_width)
        self.column2 = int(0.2*self.window_width)
        self.column3 = int(0.35*self.window_width)
        self.column4 = int(0.50*self.window_width)
        self.column5 = int(0.65*self.window_width)
        self.column6 = int(0.8*self.window_width)
        self.row1 = int(0.05*self.window_height)
        self.row2 = int(0.3*self.window_height)
        self.row3 = int(0.55*self.window_height)
        self.row4 = int(0.8*self.window_height)
        # endregion

        super().__init__()  # parent's __init__
        self.setWindowTitle("Stend manager")  # add window title
        self.resize(self.window_width, self.window_height)  # Main window size

        self.daemon1 = threading.Timer(function=self.demon, interval=5)
        self.daemon1.start()

        # Main window widgets
        # stend1
        # region
        self.stend1_base_path = 'C:\\Tandem Stends\\Stend2'   # TODO Добавь сюда путь до своего стенда
        self.stend1_name = self.stend1_base_path.split('\\')[-1]
        self.stend1_label = QLabel(self, text=f'Стенд №1 : {self.stend1_name}')
        self.stend1_label.move(self.column1, (self.row1-20))
        self.stend1_label.setFixedSize(int(0.75 * self.window_width), 20)

        self.stend1_path = QLineEdit(self.stend1_base_path, self)  # add text line
        self.stend1_path.move(self.column1, self.row1)  # move text line
        self.stend1_path.setReadOnly(True)
        self.stend1_path.setFixedSize(int(0.75 * self.window_width), 20)

        self.stend1_catalina_btn = QPushButton('Catalina log', self)
        self.stend1_catalina_btn.move(self.column1, (self.row1+30))
        self.stend1_catalina_btn.clicked.connect(lambda: self.catalina_open(self.stend1_base_path))

        self.stend1_stderr_btn = QPushButton('stderr log', self)
        self.stend1_stderr_btn.move(self.column2, (self.row1+30))
        self.stend1_stderr_btn.clicked.connect(lambda: self.stderr_open(path=self.stend1_base_path))

        self.stend1_stdout_btn = QPushButton('stdout log', self)
        self.stend1_stdout_btn.move(self.column3, (self.row1+30))
        self.stend1_stdout_btn.clicked.connect(lambda: self.stdout_open(path=self.stend1_base_path,
                                                                        name=self.stend1_name))

        self.stend1_nsisync_btn = QPushButton('NsiSync log', self)
        self.stend1_nsisync_btn.move(self.column4, (self.row1+30))
        self.stend1_nsisync_btn.clicked.connect(lambda: self.nsisync_open(self.stend1_base_path))

        self.stend1_log_dir_btn = QPushButton('Log directory', self)
        self.stend1_log_dir_btn.move(self.column5, (self.row1+30))
        self.stend1_log_dir_btn.clicked.connect(lambda: self.log_dir_open(self.stend1_base_path))

        self.stend1_clear_logs_btn = QPushButton('Clear logs', self)
        self.stend1_clear_logs_btn.move(self.column5, self.row1+60)
        self.stend1_clear_logs_btn.clicked.connect(lambda: self.clear_logs(self.stend1_base_path))

        self.stend1_edit_hibernate_properties_btn = QPushButton('Edit HP', self)
        self.stend1_edit_hibernate_properties_btn.move(self.column4, self.row1+60)
        self.stend1_edit_hibernate_properties_btn.clicked.connect(lambda:
                                                                  self.edit_hibernate_properties(self.stend1_base_path))

        self.stend1_edit_app_properties_btn = QPushButton('Edit AP', self)
        self.stend1_edit_app_properties_btn.move(self.column3, self.row1+60)
        self.stend1_edit_app_properties_btn.clicked.connect(lambda: self.edit_app_properties(self.stend1_base_path))

        self.stend1_start_btn = QPushButton('Start', self)
        self.stend1_start_btn.move(self.column1, self.row1+60)
        self.stend1_start_btn.clicked.connect(lambda: self.start_stend(self.stend1_name, self.stend1_start_btn, self.stend1_path, self.stend1_stop_btn))

        self.stend1_stop_btn = QPushButton('Stop', self)
        self.stend1_stop_btn.move(self.column2, self.row1+60)
        self.stend1_stop_btn.clicked.connect(lambda: self.stop_stend(self.stend1_name, self.stend1_start_btn, self.stend1_path, self.stend1_stop_btn))
        # endregion

        # stend2
        # region
        self.stend2_base_path = 'C:\\Tandem Stends\\StendNSI'   # TODO Добавь сюда путь до своего стенда
        self.stend2_name = self.stend2_base_path.split('\\')[-1]
        self.stend2_label = QLabel(self,  text=f'Стенд №2 : {self.stend2_name}')
        self.stend2_label.move(self.column1, (self.row2-20))
        self.stend2_label.setFixedSize(int(0.75 * self.window_width), 20)

        self.stend2_path = QLineEdit(self.stend2_base_path, self)  # add text line
        self.stend2_path.setReadOnly(True)
        self.stend2_path.move(self.column1, self.row2)  # move text line
        self.stend2_path.setFixedSize(int(0.75 * self.window_width), 20)

        self.stend2_catalina_btn = QPushButton('Catalina log', self)
        self.stend2_catalina_btn.move(self.column1, (self.row2+30))
        self.stend2_catalina_btn.clicked.connect(lambda: self.catalina_open(self.stend2_base_path))

        self.stend2_stderr_btn = QPushButton('stderr log', self)
        self.stend2_stderr_btn.move(self.column2, (self.row2+30))
        self.stend2_stderr_btn.clicked.connect(lambda: self.stderr_open(path=self.stend2_base_path))

        self.stend2_stdout_btn = QPushButton('stdout log', self)
        self.stend2_stdout_btn.move(self.column3, (self.row2+30))
        self.stend2_stdout_btn.clicked.connect(lambda: self.stdout_open(path=self.stend2_base_path,
                                                                        name=self.stend2_name))

        self.stend2_nsisync_btn = QPushButton('NsiSync log', self)
        self.stend2_nsisync_btn.move(self.column4, (self.row2+30))
        self.stend2_nsisync_btn.clicked.connect(lambda: self.nsisync_open(self.stend2_base_path))

        self.stend2_log_dir_btn = QPushButton('Log directory', self)
        self.stend2_log_dir_btn.move(self.column5, (self.row2+30))
        self.stend2_log_dir_btn.clicked.connect(lambda: self.log_dir_open(self.stend2_base_path))

        self.stend2_clear_logs_btn = QPushButton('Clear logs', self)
        self.stend2_clear_logs_btn.move(self.column5, self.row2+60)
        self.stend2_clear_logs_btn.clicked.connect(lambda: self.clear_logs(self.stend2_base_path))

        self.stend2_edit_hibernate_properties_btn = QPushButton('Edit HP', self)
        self.stend2_edit_hibernate_properties_btn.move(self.column4, self.row2+60)
        self.stend2_edit_hibernate_properties_btn.clicked.connect(lambda:
                                                                  self.edit_hibernate_properties(self.stend2_base_path))

        self.stend2_edit_app_properties_btn = QPushButton('Edit AP', self)
        self.stend2_edit_app_properties_btn.move(self.column3, self.row2+60)
        self.stend2_edit_app_properties_btn.clicked.connect(lambda: self.edit_app_properties(self.stend2_base_path))

        self.stend2_start_btn = QPushButton('Start', self)
        self.stend2_start_btn.move(self.column1, self.row2+60)
        self.stend2_start_btn.clicked.connect(lambda: self.start_stend(self.stend2_name, self.stend2_start_btn, self.stend2_path, self.stend2_stop_btn))

        self.stend2_stop_btn = QPushButton('Stop', self)
        self.stend2_stop_btn.move(self.column2, self.row2+60)
        self.stend2_stop_btn.clicked.connect(lambda: self.stop_stend(self.stend2_name, self.stend2_start_btn, self.stend2_path, self.stend2_stop_btn))
        # endregion

        # stend 3
        # region
        self.stend3_base_path = 'C:\\Tandem Stends\\tandemUNI'   # TODO Добавь сюда путь до своего стенда
        self.stend3_name = self.stend3_base_path.split('\\')[-1]
        self.stend3_label = QLabel(self,  text=f'Стенд №3 : {self.stend3_name}')
        self.stend3_label.move(self.column1, (self.row3-20))
        self.stend3_label.setFixedSize(int(0.75 * self.window_width), 20)

        self.stend3_path = QLineEdit(self.stend3_base_path, self)  # add text line
        self.stend3_path.setReadOnly(True)
        self.stend3_path.move(self.column1, self.row3)  # move text line
        self.stend3_path.setFixedSize(int(0.75 * self.window_width), 20)

        self.stend3_catalina_btn = QPushButton('Catalina log', self)
        self.stend3_catalina_btn.move(self.column1, (self.row3+30))
        self.stend3_catalina_btn.clicked.connect(lambda: self.catalina_open(self.stend3_base_path))

        self.stend3_stderr_btn = QPushButton('stderr log', self)
        self.stend3_stderr_btn.move(self.column2, (self.row3+30))
        self.stend3_stderr_btn.clicked.connect(lambda: self.stderr_open(path=self.stend3_base_path))

        self.stend3_stdout_btn = QPushButton('stdout log', self)
        self.stend3_stdout_btn.move(self.column3, (self.row3+30))
        self.stend3_stdout_btn.clicked.connect(lambda: self.stdout_open(path=self.stend3_base_path,
                                                                        name=self.stend3_name))

        self.stend3_nsisync_btn = QPushButton('NsiSync log', self)
        self.stend3_nsisync_btn.move(self.column4, (self.row3+30))
        self.stend3_nsisync_btn.clicked.connect(lambda: self.nsisync_open(self.stend3_base_path))

        self.stend3_log_dir_btn = QPushButton('Log directory', self)
        self.stend3_log_dir_btn.move(self.column5, (self.row3+30))
        self.stend3_log_dir_btn.clicked.connect(lambda: self.log_dir_open(self.stend3_base_path))

        self.stend3_clear_logs_btn = QPushButton('Clear logs', self)
        self.stend3_clear_logs_btn.move(self.column5, self.row3+60)
        self.stend3_clear_logs_btn.clicked.connect(lambda: self.clear_logs(self.stend3_base_path))

        self.stend3_edit_hibernate_properties_btn = QPushButton('Edit HP', self)
        self.stend3_edit_hibernate_properties_btn.move(self.column4, self.row3+60)
        self.stend3_edit_hibernate_properties_btn.clicked.connect(lambda:
                                                                  self.edit_hibernate_properties(self.stend3_base_path))

        self.stend3_edit_app_properties_btn = QPushButton('Edit AP', self)
        self.stend3_edit_app_properties_btn.move(self.column3, self.row3+60)
        self.stend3_edit_app_properties_btn.clicked.connect(lambda: self.edit_app_properties(self.stend3_base_path))

        self.stend3_start_btn = QPushButton('Start', self)
        self.stend3_start_btn.move(self.column1, self.row3+60)
        self.stend3_start_btn.clicked.connect(lambda: self.start_stend(self.stend3_name, self.stend3_start_btn, self.stend3_path, self.stend3_stop_btn))

        self.stend3_stop_btn = QPushButton('Stop', self)
        self.stend3_stop_btn.move(self.column2, self.row3+60)
        self.stend3_stop_btn.clicked.connect(lambda: self.stop_stend(self.stend3_name, self.stend3_start_btn, self.stend3_path, self.stend3_stop_btn))
        # endregion

        # stend 4
        # region
        self.stend4_base_path = 'C:\\Tandem Stends\\ExpStend'   # TODO Добавь сюда путь до своего стенда
        self.stend4_name = self.stend4_base_path.split('\\')[-1]
        self.stend4_label = QLabel(self,  text=f'Стенд №4 : {self.stend4_name}')
        self.stend4_label.move(self.column1, (self.row4-20))
        self.stend4_label.setFixedSize(int(0.75 * self.window_width), 20)

        self.stend4_path = QLineEdit(self.stend4_base_path, self)  # add text line
        self.stend4_path.setReadOnly(True)
        self.stend4_path.move(self.column1, self.row4)  # move text line
        self.stend4_path.setFixedSize(int(0.75 * self.window_width), 20)

        self.stend4_catalina_btn = QPushButton('Catalina log', self)
        self.stend4_catalina_btn.move(self.column1, (self.row4+30))
        self.stend4_catalina_btn.clicked.connect(lambda: self.catalina_open(self.stend4_base_path))

        self.stend4_stderr_btn = QPushButton('stderr log', self)
        self.stend4_stderr_btn.move(self.column2, (self.row4+30))
        self.stend4_stderr_btn.clicked.connect(lambda: self.stderr_open(path=self.stend4_base_path))

        self.stend4_stdout_btn = QPushButton('stdout log', self)
        self.stend4_stdout_btn.move(self.column3, (self.row4+30))
        self.stend4_stdout_btn.clicked.connect(lambda: self.stdout_open(path=self.stend4_base_path,
                                                                        name=self.stend4_name))

        self.stend4_nsisync_btn = QPushButton('NsiSync log', self)
        self.stend4_nsisync_btn.move(self.column4, (self.row4+30))
        self.stend4_nsisync_btn.clicked.connect(lambda: self.nsisync_open(self.stend4_base_path))

        self.stend4_log_dir_btn = QPushButton('Log directory', self)
        self.stend4_log_dir_btn.move(self.column5, (self.row4+30))
        self.stend4_log_dir_btn.clicked.connect(lambda: self.log_dir_open(self.stend4_base_path))

        self.stend4_clear_logs_btn = QPushButton('Clear logs', self)
        self.stend4_clear_logs_btn.move(self.column5, self.row4+60)
        self.stend4_clear_logs_btn.clicked.connect(lambda: self.clear_logs(self.stend4_base_path))

        self.stend4_edit_hibernate_properties_btn = QPushButton('Edit HP', self)
        self.stend4_edit_hibernate_properties_btn.move(self.column4, self.row4+60)
        self.stend4_edit_hibernate_properties_btn.clicked.connect(lambda:
                                                                  self.edit_hibernate_properties(self.stend4_base_path))

        self.stend4_edit_app_properties_btn = QPushButton('Edit AP', self)
        self.stend4_edit_app_properties_btn.move(self.column3, self.row4+60)
        self.stend4_edit_app_properties_btn.clicked.connect(lambda: self.edit_app_properties(self.stend4_base_path))

        self.stend4_start_btn = QPushButton('Start', self)
        self.stend4_start_btn.move(self.column1, self.row4+60)
        self.stend4_start_btn.clicked.connect(lambda: self.start_stend(self.stend4_name, self.stend4_start_btn, self.stend4_path, self.stend4_stop_btn))

        self.stend4_stop_btn = QPushButton('Stop', self)
        self.stend4_stop_btn.move(self.column2, self.row4+60)
        self.stend4_stop_btn.clicked.connect(lambda: self.stop_stend(self.stend4_name, self.stend4_start_btn, self.stend4_path, self.stend4_stop_btn))
        # endregion

    def catalina_open(self, path):
        files = os.listdir(path+'\\tomcat\\logs')
        if files:
            files = [file for file in files if file.startswith('catalina')]
            if files:
                paths = [(path+'\\tomcat\\logs\\'+file) for file in files]
                os.startfile(max(paths, key=os.path.getctime))
            else:
                self.no_such_log()
        else:
            self.empty_warning()

    def nsisync_open(self, path):
        files = os.listdir(path+'\\tomcat\\logs')
        if files:
            files = [file for file in files if file.startswith('NsiSync')]
            if files:
                paths = [(path+'\\tomcat\\logs\\'+file) for file in files]
                os.startfile(max(paths, key=os.path.getctime))
            else:
                self.no_such_log()
        else:
            self.empty_warning()

    def log_dir_open(self, path):
        try:
            os.startfile(path+'\\tomcat\\logs')
        except Exception:
            QMessageBox.information(self, 'Папка с логами не обнаружена',
                                    'По указанному пути отсуствует папка с логами, проверьте правильность пути')

    def empty_warning(self):
        QMessageBox.information(self, "Логи отсутствуют",
                                'Папка с логами пуста, убедитесь что вы правильно указали путь или запустите стенд, '
                                'чтобы логи появились')

    def no_such_log(self):
        QMessageBox.information(self, "Лог отсутствуют",
                                'Данный лог отсутствует, убедитесь что вы правильно указали путь или запустите стенд, '
                                'чтобы данный лог появился')

    def change_dir1(self):
        self.stend1_base_path = QFileDialog.getExistingDirectory()
        self.stend1_path.setText(self.stend1_base_path)

    def change_dir2(self):
        self.stend2_base_path = QFileDialog.getExistingDirectory()
        self.stend2_path.setText(self.stend2_base_path)

    def change_dir3(self):
        self.stend3_base_path = QFileDialog.getExistingDirectory()
        self.stend3_path.setText(self.stend3_base_path)
        self.stend3_name = self.stend3_base_path.split('\\')[-1]

    def stderr_open(self, path):
        print(path)
        name = path.split('\\')[-1].lower()
        print(name)
        files = os.listdir(path+'\\tomcat\\logs')
        if files:
            files = [file for file in files if file.startswith(name+'-stderr')]
            if files:
                paths = [(path+'\\tomcat\\logs\\'+file) for file in files]
                os.startfile(max(paths, key=os.path.getctime))
            else:
                self.no_such_log()
        else:
            self.empty_warning()

    def stdout_open(self, name, path):
        files = os.listdir(path+'\\tomcat\\logs')
        if files:
            files = [file for file in files if file.startswith(name.lower()+'-stdout')]
            if files:
                paths = [(path+'\\tomcat\\logs\\'+file) for file in files]
                os.startfile(max(paths, key=os.path.getctime))
            else:
                self.no_such_log()
        else:
            self.empty_warning()

    @staticmethod
    def clear_logs(path):
        for file in os.scandir(path+'\\tomcat\\logs'):
            os.remove(file.path)

    @staticmethod
    def edit_hibernate_properties(path):
        os.startfile(path+'\\config\\hibernate.properties')

    @staticmethod
    def edit_app_properties(path):
        os.startfile(path+'\\config\\app.properties')

    @staticmethod
    def start_stend(stend_name, start_btn, path_field, stop_btn):
        if win32serviceutil.QueryServiceStatus(stend_name)[1] == 4:
            pass
        else:
            win32serviceutil.StartService(stend_name)
            start_btn.setDisabled(True)
            path_field.setStyleSheet("background:lightgreen;")
            stop_btn.setDisabled(False)

    @staticmethod
    def stop_stend(stend_name, start_btn, path_field, stop_btn):
        if win32serviceutil.QueryServiceStatus(stend_name)[1] == 4:
            win32serviceutil.StopService(stend_name)
            start_btn.setDisabled(False)
            path_field.setStyleSheet("background:pink;")
            stop_btn.setDisabled(True)
        else:
            pass

    @staticmethod
    def check_service(stend_name, stend_path, stend_start_btn, stend_stop_btn):
        if win32serviceutil.QueryServiceStatus(stend_name)[1] == 4:
            stend_path.setStyleSheet("background:lightgreen;")
            stend_start_btn.setDisabled(True)
            stend_stop_btn.setDisabled(False)
        else:
            stend_path.setStyleSheet("background:pink;")
            stend_start_btn.setDisabled(False)
            stend_stop_btn.setDisabled(True)

    def demon(self):
        while True:
            self.check_service(self.stend1_name, self.stend1_path, self.stend1_start_btn, self.stend1_stop_btn)
            self.check_service(self.stend2_name, self.stend2_path, self.stend2_start_btn, self.stend2_stop_btn)
            self.check_service(self.stend3_name, self.stend3_path, self.stend3_start_btn, self.stend3_stop_btn)
            self.check_service(self.stend4_name, self.stend4_path, self.stend4_start_btn, self.stend4_stop_btn)
            time.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create app
    dlg_main = DlgMain()  # create main GUI window
    dlg_main.show()  # show window
    app.setWindowIcon(QIcon('2.ico'))
    sys.exit(app.exec_())  # exec app
