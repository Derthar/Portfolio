import os
from PyQt5.QtWidgets import *
import sys
# pyinstaller --onefile -w --icon=2.ico read_logs.py


class DlgMain(QDialog):
    def __init__(self, name):

        # set variables
        # region
        self.window_width = 700
        self.window_height = 400
        self.column1 = int(0.05*self.window_width)
        self.column2 = int(0.2*self.window_width)
        self.column3 = int(0.35*self.window_width)
        self.column4 = int(0.50*self.window_width)
        self.column5 = int(0.65*self.window_width)
        self.column6 = int(0.8*self.window_width)
        self.row1 = int(0.1*self.window_height)
        self.row2 = int(0.4*self.window_height)
        self.row3 = int(0.7*self.window_height)
        # endregion

        super().__init__()  # parent's __init__
        self.setWindowTitle("Read Logs")  # add window title
        self.resize(self.window_width, self.window_height)  # Main window size
        self.fucking_function()

        # Main window widgets
        # stend1
        # region
        self.stend1_base_path = 'D:\Stend2'   # TODO Добавь сюда путь до своего стенда
        self.stend1_name = self.stend1_base_path.split('\\')[-1]
        self.stend1_label = QLabel(self, text='Стенд №1 : ')
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
        self.stend1_stdout_btn.clicked.connect(lambda: self.stdout_open(path=self.stend1_base_path, name=self.stend1_name))

        self.stend1_nsisync_btn = QPushButton('NsiSync log', self)
        self.stend1_nsisync_btn.move(self.column4, (self.row1+30))
        self.stend1_nsisync_btn.clicked.connect(lambda: self.nsisync_open(self.stend1_base_path))

        self.stend1_log_dir_btn = QPushButton('Log directory', self)
        self.stend1_log_dir_btn.move(self.column5, (self.row1+30))
        self.stend1_log_dir_btn.clicked.connect(lambda: self.log_dir_open(self.stend1_base_path))

        # FIXME при смене стенда, не пересчитывает новое имя стенда, из-за чего не может найти логи stderr и stdout
        self.stend1_change_dir_btn = QPushButton('Выбрать другой', self)
        self.stend1_change_dir_btn.setFixedSize(120, 60)
        self.stend1_change_dir_btn.setDisabled(True)
        self.stend1_change_dir_btn.move(self.column6, self.row1)
        self.stend1_change_dir_btn.clicked.connect(lambda: self.change_dir1())
        # endregion

        # stend2
        # region
        self.stend2_base_path = 'D:\StendNSI\StendNSI'   # TODO Добавь сюда путь до своего стенда
        self.stend2_name = self.stend2_base_path.split('\\')[-1]
        self.stend2_label = QLabel(self,  text='Стенд №2 : ')
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
        self.stend2_stdout_btn.clicked.connect(lambda: self.stdout_open(path=self.stend2_base_path, name=self.stend2_name))

        self.stend2_nsisync_btn = QPushButton('NsiSync log', self)
        self.stend2_nsisync_btn.move(self.column4, (self.row2+30))
        self.stend2_nsisync_btn.clicked.connect(lambda: self.nsisync_open(self.stend2_base_path))

        self.stend2_log_dir_btn = QPushButton('Log directory', self)
        self.stend2_log_dir_btn.move(self.column5, (self.row2+30))
        self.stend2_log_dir_btn.clicked.connect(lambda: self.log_dir_open(self.stend2_base_path))

        # FIXME при смене стенда, не пересчитывает новое имя стенда, из-за чего не может найти логи stderr и stdout
        self.stend2_change_dir_btn = QPushButton('Выбрать другой', self)
        self.stend2_change_dir_btn.setFixedSize(120, 60)
        self.stend2_change_dir_btn.setDisabled(True)
        self.stend2_change_dir_btn.move(self.column6, self.row2)
        self.stend2_change_dir_btn.clicked.connect(lambda: self.change_dir2())
        # endregion

        # stend 3
        # region
        self.stend3_base_path = 'C:\Program Files\\tandemUNI'   # TODO Добавь сюда путь до своего стенда
        self.stend3_name = self.stend3_base_path.split('\\')[-1]
        self.stend3_label = QLabel(self,  text='Стенд №3 : ')
        self.stend3_label.move(self.column1, (self.row3-20))
        self.stend3_label.setFixedSize(int(0.75 * self.window_width), 20)

        self.stend3_path = QLineEdit(self.stend3_base_path, self)  # add text line
        self.stend2_path.setReadOnly(True)
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
        self.stend3_stdout_btn.clicked.connect(lambda: self.stdout_open(path=self.stend3_base_path, name=self.stend3_name))

        self.stend3_nsisync_btn = QPushButton('NsiSync log', self)
        self.stend3_nsisync_btn.move(self.column4, (self.row3+30))
        self.stend3_nsisync_btn.clicked.connect(lambda: self.nsisync_open(self.stend3_base_path))

        self.stend3_log_dir_btn = QPushButton('Log directory', self)
        self.stend3_log_dir_btn.move(self.column5, (self.row3+30))
        self.stend3_log_dir_btn.clicked.connect(lambda: self.log_dir_open(self.stend3_base_path))

        # FIXME при смене стенда, не пересчитывает новое имя стенда, из-за чего не может найти логи stderr и stdout
        self.stend3_change_dir_btn = QPushButton('Выбрать другой', self)
        self.stend3_change_dir_btn.setFixedSize(120, 60)
        self.stend3_change_dir_btn.setDisabled(True)
        self.stend3_change_dir_btn.move(self.column6, self.row3)
        self.stend3_change_dir_btn.clicked.connect(lambda: self.change_dir3())
        # endregion

    def fucking_funtion(self):
        print('Fuck you!')

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
        except:
            QMessageBox.information(self, 'Папка с логами не обнаружена', 'По указанному пути отсуствует папка с логами, проверьте правильность пути')

    def empty_warning(self):
        QMessageBox.information(self, "Логи отсутствуют", 'Папка с логами пуста, убедитесь что вы правильно указали путь или запустите стенд, чтобы логи появились')

    def no_such_log(self):
        QMessageBox.information(self, "Лог отсутствуют", 'Данный лог отсутствует, убедитесь что вы правильно указали путь или запустите стенд, чтобы данный лог появился')

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


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create app
    dlg_main = DlgMain('dlg_main')  # create main GUI window
    dlg_main.show()  # show window
    sys.exit(app.exec_())  # exec app
