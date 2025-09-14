from PySide6.QtWidgets import QMessageBox
import os
import argparse #Here in case I come back to using this

# Renames files in a sequential numerical order starting from 1
def rename_files(directory, prefix, suffix):
    try:
        target_directory_files = os.listdir(directory)
    except:
        QMessageBox.critical(None, "Error", f"The directory '{directory}' was not found.")
        return
    file_count = 1
    for filename in target_directory_files:
        current_item = os.path.join(directory, filename)
        if os.path.isfile(current_item):
            _, extension = os.path.splitext(filename)
            new_name = f"{prefix}{file_count}{suffix}{extension}"
            new_destination = os.path.join(directory, new_name)
            
            try:
                os.rename(current_item, new_destination)
                file_count += 1
            except FileNotFoundError:
                QMessageBox.critical(None, "Error", f"The file '{current_item}' was not found.")
            except PermissionError:
                QMessageBox.critical(None, "Error", f"Permission denied. Cannot rename '{current_item}'. Try to run the program as an administrator.")
            except Exception as e:
                QMessageBox.critical(None, "Error", f"An unexpected error occurred: {e}")