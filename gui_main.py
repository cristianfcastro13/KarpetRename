import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QFileDialog
from PySide6.QtCore import Qt # Import for alignment
from PySide6.QtGui import QPixmap # For image handling later
from gui_widgets import Widgets



if __name__ == "__main__":
    app = QApplication(sys.argv)
    initial_directory = None
    if len(sys.argv) > 1:
        initial_directory = sys.argv[1]

    window = Widgets(initial_directory=initial_directory)
    window.show()
    
    app.exec()