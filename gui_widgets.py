from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QApplication, QFileDialog
from PySide6.QtGui import QWindow, QAction, QIcon, QPixmap
from PySide6.QtCore import QSize, Qt, Signal, Slot
from main import rename_files
import sys
import os

def resource_path(relative_path):

    # Gets absolute path to resource, necessary codes for dev and for PyInstaller
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Widgets(QWidget):
    def __init__(self, initial_directory):
        self.current_directory = initial_directory

        #Initializes the main window and its components
        super().__init__()
        self.setup_window()
        self.live_updated_labels()
        self.before_file_layout()
        self.after_file_layout()
        self.preview_layout()
        self.navigation_layout()
        self.prefix_suffix_layout()
        self.button_rename()
        self.main_layout()

    def setup_window(self):
        # Set window properties and create window spawn point
        window_width = 330
        window_height = 400
        screen = QApplication.primaryScreen().availableGeometry()
        screen_center_x = screen.center().x()
        screen_center_y = screen.center().y()
        spawn_point_x = screen_center_x - (window_width // 2) + (screen_center_x * 0.2)
        spawn_point_y = screen_center_y - (window_height // 2)
        self.setWindowTitle("Karpet Rename")
        self.setGeometry(spawn_point_x, spawn_point_y, window_width, window_height)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon(resource_path("images/123.png")))

    def main_layout(self):
        # Set main layout
        main_v_layout = QVBoxLayout()
        main_v_layout.setAlignment(Qt.AlignCenter)
        main_v_layout.addLayout(self.preview_h_layout)
        main_v_layout.addLayout(self.navigation_v_layout)
        main_v_layout.addLayout(self.prefix_suffix_h_layout)
        main_v_layout.addWidget(self.rename_button)
        self.setLayout(main_v_layout)

    def preview_layout(self):
        # Set preview layout
        self.preview_h_layout = QHBoxLayout()
        self.preview_h_layout.setAlignment(Qt.AlignCenter)

        self.preview_h_layout.addLayout(self.before_file_v_layout)

        right_arrow_label = QLabel()
        right_arrow_label.setPixmap(QPixmap(resource_path("images/right_arrow.png")).scaled(45, 45, Qt.KeepAspectRatio))
        right_arrow_label.setAlignment(Qt.AlignCenter)
        self.preview_h_layout.addWidget(right_arrow_label)

        self.preview_h_layout.addLayout(self.after_file_v_layout)
    
    def before_file_layout(self):
        # Set 'before' file layout
        self.before_file_v_layout = QVBoxLayout()
        self.before_file_v_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        before_file_pic_label = QLabel()
        before_file_pic_label.setPixmap(QPixmap(resource_path("images/file_icon.png")).scaled(92, 92, Qt.KeepAspectRatio))
        before_file_pic_label.setAlignment(Qt.AlignCenter)
        self.before_file_v_layout.addWidget(before_file_pic_label)

        default_file_label = QLabel("Your_Messy_File_ Name_2612_127")
        default_file_label.setWordWrap(True)
        default_file_label.setAlignment(Qt.AlignCenter)
        default_file_label.setFixedWidth(100)
        self.before_file_v_layout.addWidget(default_file_label)
    
    def after_file_layout(self):
        # Set 'after' file layout
        self.after_file_v_layout = QVBoxLayout()
        self.after_file_v_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        after_file_pic_label = QLabel()
        after_file_pic_label.setPixmap(QPixmap(resource_path("images/file_icon.png")).scaled(92, 92, Qt.KeepAspectRatio))
        after_file_pic_label.setAlignment(Qt.AlignCenter)
        self.after_file_v_layout.addWidget(after_file_pic_label)

        self.after_file_v_layout.addLayout(self.updated_labels_layout)

    def live_updated_labels(self):
        # Live-updated labels for after file layout
        self.updated_labels_layout = QHBoxLayout()
        self.updated_labels_layout.setAlignment(Qt.AlignCenter)
        
        # Prefix live-updated label
        self.prefix_label = QLabel("")
        self.prefix_label.setAlignment(Qt.AlignCenter)
        self.prefix_label.setFixedWidth(48)
        self.updated_labels_layout.addWidget(self.prefix_label)

        # Changing number live-updated label
        self.number_label = QLabel("N")
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setFixedWidth(7)
        self.updated_labels_layout.addWidget(self.number_label)

        # Suffix live-updated label
        self.suffix_label = QLabel("")
        self.suffix_label.setAlignment(Qt.AlignCenter)
        self.suffix_label.setFixedWidth(48)
        self.updated_labels_layout.addWidget(self.suffix_label)

    def navigation_layout(self):
        # Set navigation layout
        self.navigation_v_layout = QVBoxLayout()
        self.navigation_v_layout.setAlignment(Qt.AlignCenter)

        # Add text label for navigation
        navigation_label = QLabel("You are renaming all files in:")
        navigation_label.setAlignment(Qt.AlignCenter)
        self.navigation_v_layout.addWidget(navigation_label)

        # Add text label that reflects selected folder
        if not self.current_directory:
            self.selected_folder_label = QLabel("Folder Path")
            self.selected_folder_label.setAlignment(Qt.AlignCenter)
            self.selected_folder_label.setFixedWidth(220)
            self.navigation_v_layout.addWidget(self.selected_folder_label)
        else:
            self.selected_folder_label = QLabel(self.current_directory)
            self.selected_folder_label.setAlignment(Qt.AlignCenter)
            self.selected_folder_label.setFixedWidth(220)
            self.navigation_v_layout.addWidget(self.selected_folder_label)

        browse_button = QPushButton("Browse...")
        browse_button.clicked.connect(self.browse_directory)
        self.navigation_v_layout.addWidget(browse_button)

    def prefix_suffix_layout(self):
        # Set prefix / suffix layout
        self.prefix_suffix_h_layout = QHBoxLayout()
        self.prefix_suffix_h_layout.setAlignment(Qt.AlignCenter)

        # Prefix entry
        self.prefix_entry = QLineEdit()
        self.prefix_entry.setPlaceholderText("Prefix")
        self.prefix_entry.textChanged.connect(self.update_prefix_label)
        self.prefix_suffix_h_layout.addWidget(self.prefix_entry)

        # Suffix entry
        self.suffix_entry = QLineEdit()
        self.suffix_entry.setPlaceholderText("Suffix")
        self.suffix_entry.textChanged.connect(self.update_suffix_label)
        self.prefix_suffix_h_layout.addWidget(self.suffix_entry)

    def button_rename(self):
        # Set 'Rename' button
        self.rename_button = QPushButton("Rename")
        self.rename_button.clicked.connect(self.on_rename_clicked)

    def on_rename_clicked(self):

        folder = self.current_directory
        # Get the prefix and suffix from the input fields
        prefix = self.prefix_entry.text()
        suffix = self.suffix_entry.text()

        # To avoid running the rename_files function with an empty folder
        if not folder:
            QMessageBox.warning(self, "Warning", "Please select a folder to rename files.")
            return
        
        # Call the rename_files function with the provided parameters
        try:
            rename_files(directory=folder, prefix=prefix, suffix=suffix)
            QMessageBox.information(self, "Success", "Files have been renamed successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while renaming files:\n{str(e)}")

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Folder")
        if directory:
            self.current_directory = directory
            self.selected_folder_label.setText(directory)
    
    def update_prefix_label(self, new_text):
        self.prefix_label.setText(f"{new_text}")

    def update_suffix_label(self, new_text):
        self.suffix_label.setText(f"{new_text}")