from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QApplication, QFileDialog
from PySide6.QtGui import QWindow, QAction, QIcon, QPixmap
from PySide6.QtCore import QSize, Qt, Signal, Slot
from main import rename_files

class Widgets(QWidget):
    def __init__(self):
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
        self.setWindowIcon(QIcon("images/123.png"))

    # NOTE: COMPLETED, NO NEED TO CONNECT TO ANYTHING
    def main_layout(self):
        # Set main layout
        main_v_layout = QVBoxLayout()
        main_v_layout.setAlignment(Qt.AlignCenter)
        main_v_layout.addLayout(self.preview_h_layout)
        main_v_layout.addLayout(self.navigation_v_layout)
        main_v_layout.addLayout(self.prefix_suffix_h_layout)
        main_v_layout.addWidget(self.button_rename)
        self.setLayout(main_v_layout)

    # NOTE: COMPLETED, NO NEED TO CONNECT TO ANYTHING
    def preview_layout(self):
        # Set preview layout
        self.preview_h_layout = QHBoxLayout()
        self.preview_h_layout.setAlignment(Qt.AlignCenter)

        self.preview_h_layout.addLayout(self.before_file_v_layout)

        right_arrow_label = QLabel()
        right_arrow_label.setPixmap(QPixmap("images/right_arrow.png").scaled(45, 45, Qt.KeepAspectRatio))
        right_arrow_label.setAlignment(Qt.AlignCenter)
        self.preview_h_layout.addWidget(right_arrow_label)

        self.preview_h_layout.addLayout(self.after_file_v_layout)

    # NOTE: COMPLETED, NO NEED TO CONNECT TO ANYTHING
    def before_file_layout(self):
        # Set 'before' file layout
        self.before_file_v_layout = QVBoxLayout()
        self.before_file_v_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        before_file_pic_label = QLabel()
        before_file_pic_label.setPixmap(QPixmap("images/file_icon.png").scaled(92, 92, Qt.KeepAspectRatio))
        before_file_pic_label.setAlignment(Qt.AlignCenter)
        self.before_file_v_layout.addWidget(before_file_pic_label)

        default_file_label = QLabel("Your_Messy_File_ Name_2612_127")
        default_file_label.setWordWrap(True)
        default_file_label.setAlignment(Qt.AlignCenter)
        default_file_label.setFixedWidth(100)
        self.before_file_v_layout.addWidget(default_file_label)

    # NOTE: COMPLETED, NO NEED TO CONNECT TO ANYTHING
    def after_file_layout(self):
        # Set 'after' file layout
        self.after_file_v_layout = QVBoxLayout()
        self.after_file_v_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        after_file_pic_label = QLabel()
        after_file_pic_label.setPixmap(QPixmap("images/file_icon.png").scaled(92, 92, Qt.KeepAspectRatio))
        after_file_pic_label.setAlignment(Qt.AlignCenter)
        self.after_file_v_layout.addWidget(after_file_pic_label)

        self.after_file_v_layout.addLayout(self.updated_labels_layout)

    # NOTE: COMPLETED, NO NEED TO CONNECT TO ANYTHING
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

    # FIXME: self.selected_folder_label NEEDS TO BE CONNECTED TO MAIN LOGIC
    def navigation_layout(self):
        # Set navigation layout
        self.navigation_v_layout = QVBoxLayout()
        self.navigation_v_layout.setAlignment(Qt.AlignCenter)

        # Add text label for navigation
        navigation_label = QLabel("You are renaming all files in:")
        navigation_label.setAlignment(Qt.AlignCenter)
        self.navigation_v_layout.addWidget(navigation_label)

        # Add text label that reflects selected folder
        self.selected_folder_label = QLabel("Folder Path")
        self.selected_folder_label.setAlignment(Qt.AlignCenter)
        self.selected_folder_label.setFixedWidth(220)
        self.navigation_v_layout.addWidget(self.selected_folder_label)

    # FIXME: NEEDS TO BE CONNECTED TO MAIN LOGIC
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

    # FIXME: NEEDS TO BE CONNECTED TO MAIN LOGIC
    def button_rename(self):
        # Set 'Rename' button
        self.button_rename = QPushButton("Rename")
        #button_rename.clicked.connect(self.rename_files)

    def on_rename_clicked(self):
        

    def update_prefix_label(self, new_text):
        self.prefix_label.setText(f"{new_text}")

    def update_suffix_label(self, new_text):
        self.suffix_label.setText(f"{new_text}")