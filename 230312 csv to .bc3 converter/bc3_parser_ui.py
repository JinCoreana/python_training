import time
import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QProgressBar, QFileDialog

class Converter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Converter")
        self.setGeometry(100, 100, 400, 250)
        self.file_path_label = QLabel("Enter file path:", self)
        self.file_path_label.setGeometry(20, 20, 100, 20)
        self.file_path_input = QLineEdit(self)
        self.file_path_input.setGeometry(120, 20, 200, 20)
        self.browse_button = QPushButton("Browse", self)
        self.browse_button.setGeometry(330, 20, 50, 20)
        self.browse_button.clicked.connect(self.browse_file)
        self.convert_button = QPushButton("Convert", self)
        self.convert_button.setGeometry(120, 60, 80, 30)
        self.convert_button.clicked.connect(self.convert_file)
        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setGeometry(220, 60, 80, 30)
        self.cancel_button.setStyleSheet("background-color: pink;")
        self.cancel_button.clicked.connect(self.close)
        self.progress_label = QLabel("Converting...", self)
        self.progress_label.setGeometry(20, 100, 100, 20)
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(120, 100, 200, 20)
        self.progress_bar.setValue(0)
        self.show()

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_path:
            self.file_path_input.setText(file_path)

    def convert_file(self):
        self.convert_button.setDisabled(True)
        self.cancel_button.setDisabled(False)
        self.progress_bar.setValue(0)
        self.progress_bar.setHidden(False)
        file_path = self.file_path_input.text()
        if not file_path:
            print("Please specify a filename to import.")
            return
        print(f"Converting {file_path} to .bc3 format")
        self.progress_label.setText("Converting...")
        self.thread = ConversionThread(file_path)
        self.thread.progress_update.connect(self.update_progress)
        self.thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def closeEvent(self, event):
        if hasattr(self, 'thread'):
            self.thread.terminate()
        event.accept()

class ConversionThread(QThread):
    progress_update = pyqtSignal(int)

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        start_time = time.time()
        today_date = time.strftime("%d%m%y")
        with open(self.file_path, 'r', encoding='utf-16le') as f:
            data = f.readlines()
        codes = ''
        output = ''
        # Header record
        output += '~V|SOFT S.A.|FIEBDC-3/2002|Presto 8.8||ANSI|\n'
        output += '~K|\\2\\2\\3\\2\\2\\2\\2\\EUR\\|0|\n'
        output += f'~C|PROYECTO##|||0|{today_date}|0|\n'
        output += '~D|PROYECTO##|01\\1\\1\\|\n'
        output += f'~C|PROYECTO##||{filename.rstrip(".txt")}|0|{today_date}|0|\n'

