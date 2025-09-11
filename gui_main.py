import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from gui_widgets import Widgets
from main import rename_files

if __name__ == "__main__":
    app = QApplication(sys.argv)
    initial_directory = None
    if len(sys.argv) > 1:
        initial_directory = sys.argv[1]
        


        # TODO: Remove these debugging lines later
        # QMessageBox.information(None, "Info", f"The first argument is: {sys.argv[1]}")
        # if len(sys.argv) > 2:
        #     QMessageBox.information(None, "Info", f"The second argument is: {sys.argv[2]}") #Debugging line to show the second argument passed in from the context menu
        # if len(sys.argv) > 3:
        #     QMessageBox.information(None, "Info", f"The third argument is: {sys.argv[3]}")

    if (len(sys.argv) > 2):
        if (sys.argv[2] == "fast"):
            # Call the rename_files function directly with default prefix and suffix
            rename_files(directory=initial_directory, prefix="", suffix="")
            sys.exit(0)  # Exit the program after renaming files

    window = Widgets(initial_directory=initial_directory)
    window.show()
    
    app.exec()