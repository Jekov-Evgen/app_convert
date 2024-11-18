from PyQt6.QtCore import Qt, QStandardPaths
import os
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QWidget, QPushButton, QFileDialog
from GUI.style import CONST_MAIN_WINDOW
from Logik.file_processing import get_format, pdf_to_word

def format_selection(fr : str, path):
    formats = {'pdf' : pdf_to_word}
    
    result = formats.get(fr)
    desktop = os.path.join(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation), "output.docx")
    result(path, desktop)
    
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Конвектор")
        self.setFixedSize(400, 400)
        self.setStyleSheet(CONST_MAIN_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Выберите нужный вам файл")
        choice = QPushButton(text="Выбрать")
        choice.clicked.connect(self.file_selection)
        
        control_UI.addWidget(instructions, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(choice)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def file_selection(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выбор файла",                 
            "C:/",                         
            "PDF файлы (*.pdf)"    
        )
        
        format = get_format(file_path)
        
        format_selection(format[1], file_path)