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


    # TODO:THIS
    #I'm guessing this is where I interrupt the program before it opens the GUI and directly call rename_files form main.py
    #Probably need a try except block within an if statement to check if the program was called with the 'fast' arguments within the context menu
    window = Widgets(initial_directory=initial_directory)  #This within the try except block?
    window.show() #This within the try except block?
    
    app.exec()