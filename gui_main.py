import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from gui_widgets import Widgets
from main import rename_files

if __name__ == "__main__":
    app = QApplication(sys.argv)
    initial_directory = None

    # If the program was opened with a right-click context menu it will pass the target directory as an argument
    if len(sys.argv) > 1:
        initial_directory = sys.argv[1]

        # If the program was as 'Simple Karpet Rename' context menu entry, it will pass "fast" as a second argument and skip the GUI
        if (len(sys.argv) > 2):
            if (sys.argv[2] == "fast"):
                # Call the rename_files function directly with default prefix and suffix
                rename_files(directory=initial_directory, prefix="", suffix="")
                sys.exit(0)  # Exit the program after renaming files

    window = Widgets(initial_directory=initial_directory)
    window.show()
    
    app.exec()