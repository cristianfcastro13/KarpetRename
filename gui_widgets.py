from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QApplication
from PySide6.QtGui import QWindow, QAction, QIcon, QPixmap
from PySide6.QtCore import QSize, Qt
import sys



class Widgets(QWidget):
    def __init__(self):
        super().__init__()

        # Set window dimensions and create window spawn point
        window_width = 330
        window_height = 400
        screen = QApplication.primaryScreen().availableGeometry()
        screen_center_x = screen.center().x()
        screen_center_y = screen.center().y()
        spawn_point_x = screen_center_x - (window_width // 2) + (screen_center_x * 0.2)
        spawn_point_y = screen_center_y - (window_height // 2)

        # Set window properties
        self.setWindowTitle("Karpet Rename")
        self.setGeometry(spawn_point_x, spawn_point_y, window_width, window_height)
        self.setWindowIcon(QIcon("images/123.png"))

        #Create before and after file pictures
        file_pic_label = QLabel("images/file_icon.png")
        









        # Set 'Rename' button
        button_rename = QPushButton("Rename")
        button_rename.clicked
        


        # Set 'before' file layout
        before_file_v_layout = QVBoxLayout()
        # TODO: Add 'before' file picture
        # TODO: Add 'before' file label

        # Set 'after' file layout
        after_file_v_layout = QVBoxLayout()
        # TODO: Add 'after' file picture
        # TODO: Add 'after' file label

        # Set preview layout
        preview_h_layout = QHBoxLayout()
        preview_h_layout.setAlignment(Qt.AlignCenter)
        preview_h_layout.addLayout(before_file_v_layout)
        # TODO: Add right arrow picture
        preview_h_layout.addLayout(after_file_v_layout)

        # Set navigation layout
        navigation_v_layout = QVBoxLayout()
        # TODO: Add navigation label
        # TODO: Add browser navigation

        # Set prefix / suffix layout
        prefix_suffix_h_layout = QHBoxLayout()
        # TODO: Add prefix entry
        # TODO: Add suffix entry


        # Set main layout
        main_v_layout = QHBoxLayout()
        main_v_layout.setAlignment(Qt.AlignCenter)
        main_v_layout.addLayout(navigation_v_layout)
        main_v_layout.addLayout(preview_h_layout)
        main_v_layout.addLayout(prefix_suffix_h_layout)
        main_v_layout.addWidget(button_rename)
        self.setLayout(main_v_layout)


