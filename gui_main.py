import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QFileDialog
from PySide6.QtCore import Qt # Import for alignment
from PySide6.QtGui import QPixmap # For image handling later
from gui_widgets import Widgets



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widgets()
    window.show()
    app.exec()